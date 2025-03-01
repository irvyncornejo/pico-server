base:str = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%title%</title>
    <!-- Tailwind CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-900 text-gray-100">
    <!-- Modal Trigger -->
    <div class="fixed bottom-4 right-4">
        <button class="bg-blue-500 text-white p-4 rounded-full shadow-lg" onclick="openModal()">+</button>
    </div>

    <!-- Modal Structure -->
    <div id="modal" class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center hidden">
        <form action="./component">
            <div class="bg-gray-800 rounded-lg shadow-lg p-8 w-full max-w-md">
                <h2 class="text-2xl font-bold mb-4 text-blue-300">Nuevo componente</h2>
                <div class="mb-4">
                    <label for="component_name" class="block text-gray-400">Nombre</label>
                    <input 
                        id="component_name"
                        type="text"
                        class="mt-1 block w-full border-gray-600 bg-gray-700 text-gray-100 rounded-md shadow-sm"
                        name="name"
                    >
                </div>
                <div class="mb-4">
                    <label for="description" class="block text-gray-400">Descripción</label>
                    <input
                        id="description"
                        type="text"
                        class="mt-1 block w-full border-gray-600 bg-gray-700 text-gray-100 rounded-md shadow-sm"
                        name="description"
                    >
                </div>
                <div class="mb-4">
                    <label for="component_type" class="block text-gray-400">Selecciona tipo de componente</label>
                    <select
                        id="component_type"
                        class="mt-1 block w-full border-gray-600 bg-gray-700 text-gray-100 rounded-md shadow-sm"
                        name="type"
                    >
                        <option value="" disabled selected>Componentes</option>
                        <option value="1">Estado Simple</option>
                        <option value="2">Control PWM</option>
                        <option value="3">NeoPixel</option>
                    </select>
                </div>
                <div class="mb-4">
                    <label for="pin_select" class="block text-gray-400">Selecciona un pin</label>
                    <select
                        id="pin_select"
                        class="mt-1 block w-full border-gray-600 bg-gray-700 text-gray-100 rounded-md shadow-sm"
                        name="pin"
                    >
                        <option value="" disabled selected>Pin</option>
                        %gpio_options%
                    </select>
                </div>
                <div class="mb-4">
                    <label for="inverted" class="block text-gray-400">¿Maneja Lógica invertida?</label>
                    <select
                        id="inverted_select"
                        class="mt-1 block w-full border-gray-600 bg-gray-700 text-gray-100 rounded-md shadow-sm"
                        name="inverted"
                    >
                        <option value="" disabled selected>Lógica Invertida</option>
                        <option value="1">No</option>
                        <option value="0">Sí</option>
                    </select>
                </div>
                <div class="flex justify-end">
                    <button type="button" class="bg-gray-500 text-white px-4 py-2 rounded mr-2" onclick="closeModal()">Cancelar</button>
                    <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Enviar</button>
                </div>
                
            </div>
        </form>
    </div>

    <div class="container mx-auto p-4">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-bold text-blue-400">%title%</h1>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            %components%
        </div>
    </div>

    <script>
        function openModal() {
            document.getElementById("modal").classList.remove("hidden");
        }

        function closeModal() {
            document.getElementById("modal").classList.add("hidden");
        }

        function updateColor() {
            const colorPicker = document.getElementById("colorPicker");
            const selectedColor = document.getElementById("selectedColor");
            selectedColor.textContent = colorPicker.value;
        }

        function updateFloatValue() {
            const floatInput = document.getElementById("floatInput");
            const floatValue = document.getElementById("floatValue");
            floatValue.textContent = parseFloat(floatInput.value).toFixed(2);
        }

    </script>
</body>
</html>
'''
