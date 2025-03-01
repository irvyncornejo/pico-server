from gpiopico import (
    SimpleDigitalControl,
    FullDigitalControl,
    RGB,
    NeoPixel
)


class Component:
    def __init__(
        self,
        name:str,
        pin:str,
        type_component:str,
        reverse_logic=False
    )->None:
        self.name = name
        self.pin = pin
        self.type_component = type_component
        self.reverse_logic = reverse_logic
        self.html_component = self._get_html_component()
        self.hardware_component = self._hardware_component()

    def _hardware_component(self):
        _hardware = {
            '1': lambda : SimpleDigitalControl(pin=self.pin, inverted_logic=self.reverse_logic),
            '2': lambda : FullDigitalControl(pin=self.pin, inverted_logic=self.reverse_logic, limit_range=100),
            '3': lambda : NeoPixel(pin=self.pin, lenght=8)
        }
        return _hardware[self.type_component]()

    def _get_html_component(self)->str:
        html_components = {
            '1': lambda : f'''
                <div class="bg-gray-800 shadow-md rounded-lg p-4 relative">
                    <h2 class="text-xl font-semibold mb-2 text-blue-300">{self.name}</h2>
                    <p class="text-gray-400 mb-4">Status: <span class="font-bold text-yellow-400">%state%</span></p>
                    <div class="flex justify-between">
                        <form action="./gpio">
                            <input type="hidden" name="pin" value="{self.pin}">
                            <input type="hidden" name="type" value="simple">
                            <button class="bg-blue-500 text-white px-4 py-2 rounded" type="submit" name="state" value="ON">ON</button>
                        </form>
                        <form action="./gpio">
                            <input type="hidden" name="pin" value="{self.pin}">
                            <input type="hidden" name="type" value="simple">
                            <button class="bg-red-500 text-white px-4 py-2 rounded" type="submit" name="state" value="OFF">OFF</button>
                        </form>
                    </div>
                    <form action="./delete">
                        <input type="hidden" name="pin" value="{self.pin}">
                        <button class="absolute top-2 right-2 text-gray-400 hover:text-gray-100" type="submit">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                            </svg>
                        </button>
                    </form>
                </div>
            ''',
            '2': lambda : f'''
                <div class="bg-gray-800 shadow-md rounded-lg p-4 relative">
                    <h2 class="text-xl font-semibold mb-2 text-blue-300">{self.name}</h2>
                    <p class="text-gray-400 mb-4">Brightness: <span class="font-bold text-yellow-400">%state% %</span></p>
                    <div class="flex justify-between">
                        <form action="./gpio">
                            <input type="hidden" name="pin" value="{self.pin}">
                            <input type="hidden" name="type" value="slider">
                            <input type="range" min="0" max="100" value="%state%" class="w-full" name="state" id="brightness">
                            <button class="bg-blue-500 text-white px-4 py-2 rounded mt-2" type="submit">Enviar</button>
                        </form>
                    </div>
                    <form action="./delete">
                        <input type="hidden" name="pin" value={self.pin}>
                        <button class="absolute top-2 right-2 text-gray-400 hover:text-gray-100" type="submit">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                            </svg>
                        </button>
                    </form>
                </div>
            ''',
            '3': lambda : f'''
                <div class="bg-gray-800 shadow-md rounded-lg p-4 relative">
                    <h2 class="text-xl font-semibold mb-2 text-blue-300">{self.name}</h2>
                    <p class="text-gray-400 mb-4">Color: <span class="font-bold" id="selectedColor">%state%</span></p>
                    <div class="flex justify-between">
                        <form action="./gpio">
                            <input type="hidden" name="pin" value={self.pin}>
                            <input type="hidden" name="type" value="rgb">
                            <input type="color" class="w-full" name="state" value="%state%" id="colorPicker" onchange="updateColor()">
                            <button class="bg-blue-500 text-white px-4 py-2 rounded mt-2" type="submit">Enviar</button>
                        </form>
                    </div>
                    <form action="./delete">
                        <input type="hidden" name="pin" value={self.pin}>
                        <button class="absolute top-2 right-2 text-gray-400 hover:text-gray-100" type="submit">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                            </svg>
                        </button>
                    </form>
                </div>
            '''
        }
        return html_components[self.type_component]()
