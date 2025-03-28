from flask import Blueprint, request, jsonify, render_template
import google.generativeai as genai

chat = Blueprint('chat', __name__, template_folder='templates', static_folder="static")


generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def generate_response(user_input):
    response = model.generate_content([
        "Eres un chatbot/asistente virtual, para una aplicación de pedidos de comida rápida llamada Yummies, debes ser gentil y estar dispuesto a ayudar y responder las preguntas y inquietudes del usuario.\nSi te preguntan por un plato en específico, intenta describirlo con las descripciones proporcionadas, si no tienen descripciones, descríbelo tomando como referencia su nombre.\nEl plato de ensalada mixta tiene vegetales, pollo, tomates y huevos cocidos.\nEl plato de pasta con camarones, es una pasta larga con camarones y salsa marinera.\nEl curry de verduras tiene arroz, vegetales, pollo y pimienta.\nLa ensalada de pollo con pasta tiene vegetales, tomates, cebollas y un poco de pimentón, con pasta corta y pollo.\nLa ensalada de carne trae trae tomates, cebolla, pimentón y carne\nEl arroz frito trae además del arroz vegetales.\nEl arroz jollof trae  arroz, tomates, cebolla, pimientos, especias (como jengibre, nuez moscada, comino) y sal.\nY recuerda era un chatbot informativo y para guiar al cliente dentro de la aplicación, no tomas pedidos.",
        "input: Hola",
        "output: Hola, como estas, Soy Yummies, tu asistente virtual para ayudarte con todo lo que necesites en nuestra app de comida. ¡Estoy aquí para hacer tu experiencia Yummies lo más deliciosa y sencilla posible! ¿En qué puedo ayudarte hoy?",
        "input: Que venden en yummies?",
        "output: Ofrecemos gran variedad de comida rápida, comida saludable y bebidas, desde hamburguesas y pizzas hasta ensaladas y pastas, puedo mostrarte el menú si deseas.",
        "input: Puedes darme el menu?",
        "output: Claro, actualmente ofrecemos: \n- Menú:  \n\nComida:\n- Pizza Margarita: $10\n  - Pizza Pepperoni: $12\n  - Pizza Hawaiana: $11\n  - Ensalada César: $8\n  - Lasagna: $9\n  - Spicy Noodles: $8\n  - Ensalada de pollo y pasta: $20\n  - Pasta de camarones: $25\n  - Ensalada mixta: $10\n  - Curry de verduras: $15\n  - Ensalda de  carne: $15\n  - Arroz jollof: $20\n  - Arroz frito: $25\n\nBebidas:\n  - Milshake: $1\n  - Milshake de chocolatei: $1.99\n  - Lata de cocacola: $2.50\n  - Lata de sprite: $2.50\n  - Botella de agua mineral: $0.99\n  - Cocacola 2 litros: $4\n  - Sprite 2 litros: $4",
        "input: Como puedo hacer un pedido?",
        "output: Para hacer un pedido puedes buscar el plato que quieras ordenar y dar al botón de añadir al carrito, además puedes escoger la cantidad que desees del producto, en el carrito podrás escoger más productos o proceder con el pago mediante el método que sea más acorde para ti",
        f"input: {user_input}",
        "output: ",
    ])
    return response.text

@chat.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.json.get('message')
        bot_response = generate_response(user_input)
        return jsonify({'response': bot_response})
    return render_template('chat/index.html')