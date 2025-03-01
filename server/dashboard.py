from components import Component
from templates import base

def color_util(hex_color:str)->str:
    return hex_color.replace('%23', '')


class Dashboard:
    def __init__(self, component:Component, title='IoT Dashboard')->None:
        self._title = title
        self._components = []
        self._component = component
        self._in_use_gpio = set([])
        self._valid_gpio = set([
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28
        ])

    @property
    def valid_components(self):
        return self._valid_pins

    @property
    def components(self):
        return self._components

    def _create_gpio_options(self)->str:
        return ' '.join([f'<option value="{gpio}">{gpio}</option>' for gpio in self._valid_gpio])

    def _handler_hardware(self, hardware_component, state:str, type_component:str)->None:
        print(type_component)
        if type_component == '1':
            print(state)
            _state = True if state == 'ON' else False
            hardware_component.change_state(_state)
        elif type_component == '2':
            _state = int(state)
            hardware_component.pwm_value(_state)
        elif type_component == '3':
            print(state)
            state = state.replace('%23', '#')
            _state = [color_util(state)]*8
            hardware_component.write(_state)
        else:
            pass

    def process_requests(self, path:str):
        
        def _convert_params(params:str)->dict:
            return {x[0] : x[1] for x in [x.split("=") for x in params.split("&") ]}
        
        try:
            resources = path.split('/')[1]
            print(resources)
            if 'favicon.ico' in resources:
                return None

            elif 'gpio' in resources:
                params = _convert_params(resources.split('?')[1])
                self.handler_state(int(params['pin']), params['state'].replace('%23', '#'))

            elif 'component' in resources:
                params = _convert_params(resources.split('?')[1])
                self.create(params)

            elif 'delete' in resources:
                params = _convert_params(resources.split('?')[1])
                self.delete(params)

            elif 'templates' in resources:
                pass

            else:
                pass

        except Exception as e:
            print(f'Error en el procesamiento, {e}')
            return None

    def handler_state(self, pin:int, state:str)->None:
        for idx, component in enumerate(self._components):
            if component['pin'] == pin:
                print(f'Actualizando componente {pin}')
                _component = self._components[idx]
                _component['name']
                result = {
                 'name': _component['name'],
                 'state': state,
                 'pin': pin,
                 'type_component': _component['type_component'],
                 'reverse_logic': _component['reverse_logic'],
                 'html_component': _component['html_component'],
                 'html_component_show': _component['html_component'].replace('%state%', state),
                 'hardware_component': _component['hardware_component']
                }

                self._components[idx] = result

                self._handler_hardware(
                    hardware_component=result['hardware_component'],
                    state=result['state'],
                    type_component=result['type_component']
                )

    def show(self, temperature:float)->str:
        def _process_components()->str:
            _components = ''
            for elem in self._components:
                _component_html = (
                    elem['html_component_show'] if 'html_component_show' in list(elem.keys()) else elem['html_component']
                )
                _components += _component_html   
            return _components

        return str(base).replace('%components%', _process_components()).replace('gpio_options%', self._create_gpio_options()).replace('%title%', self._title)

    def delete(self, form:dict)->None:
        try:
            pin = int(form.get('pin'))
        
            if pin in self._in_use_gpio:
                self._in_use_gpio.remove(pin)
                self._valid_gpio.add(pin)

                for i, component in enumerate(self._components):
                    if int(component['pin']) == pin:
                        del self._components[i]
                        break
                print(f'Componente borrado de forma correcta!!!')
                return True
    
        except Exception as e:
            print(f'Error al borrar componente')
            return None
            

    def create(self, form:dict)->None:
        try:
            name = form.get('name', '').strip().replace('+', ' ')
            type_component = form.get('type', '1').strip()
            pin = int(form.get('pin', '0').strip())
            reverse_logic = int(form.get('inverted', '0').strip())

            if pin in self._in_use_gpio:
                print(f'GPIO {pin} en Uso')
                return None
            print(bool(reverse_logic))
            component = self._component(
                name=name,
                pin=pin,
                type_component=type_component,
                reverse_logic= bool(reverse_logic)
            ).__dict__
            self._components.append(component)
            self._in_use_gpio.add(pin)
            self._valid_gpio.remove(pin)

            return True

        except Exception as e:
            print(f'Error al crear el componente, {e}')
            return None


    def run(self)->None:
        pass
