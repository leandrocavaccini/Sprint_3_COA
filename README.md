# Sprint_3_COA

# Controle Inteligente de Sessão de Recarga

## Sobre o Projeto
Este é um protótipo educacional desenvolvido para simular um sistema inteligente de controle de recarga, inspirado no conceito do **GoodWe Smart Energy Controller**. Utilizando um **Raspberry Pi Pico** programado em **MicroPython**, o sistema monitora e decide o status de uma sessão de recarga com base na relação entre a energia gerada (ex: painéis solares) e o consumo da residência.

## Arquitetura de Computadores Aplicada
O código e o hardware foram estruturados para demonstrar o fluxo básico de um sistema computacional:
* **Entrada de Dados:** Os valores de "Geração" e "Consumo" atuam como os dados de entrada do sistema.
* **Processamento e Memória:** A CPU do Raspberry Pi processa o cálculo matemático (`Energia Disponível = Geração - Consumo`) utilizando a memória para alocar as variáveis.
* **Saída (E/S):** A resposta do processamento é enviada para os dispositivos de saída (3 LEDs indicadores) e para o Monitor Serial. O sistema também converte e exibe os dados manipulados em formatos Decimal, Binário e Hexadecimal.

## Estados de Recarga
O sistema atende a 3 situações operacionais distintas:
* **LED Verde (Recarga Autorizada):** Há energia suficiente (Disponível $\ge$ 2500W).
* **LED Amarelo (Recarga Reduzida):** Energia limitada, permite carga parcial (Disponível $> 0$W e $< 2500$W).
* **LED Vermelho (Recarga Bloqueada):** Energia insuficiente ou déficit (Disponível $\le 0$W).

## Componentes do Protótipo
* 1x Placa Raspberry Pi Pico
* 3x LEDs (Verde, Amarelo e Vermelho)
* 3x Resistores (220 $\Omega$)
* Jumpers para conexão

## Link do projeto: 
* https://wokwi.com/projects/475280846199918593
