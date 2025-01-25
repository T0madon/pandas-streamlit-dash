from gradio import Interface

def somar(num1, num2):
    return num1 + num2

iface = Interface(
    fn=somar,
    inputs=["number", "number"],
    outputs="number",
    title="Calculadora de Soma",
    description="Insira dois números para obter a soma",
    theme="default"
)

iface.launch()