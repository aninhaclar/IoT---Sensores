# IoT --- Projetos com Sensores e ESP32

Este repositório reúne **projetos de sensores utilizando ESP32**, cada um com seu próprio circuito, código e demonstração.  
Os projetos foram desenvolvidos para mostrar aplicações básicas de **IoT** com indicadores LED.

---

## Projeto 1 - LDR e Indicador LED

Este projeto detecta **luminosidade no ambiente**.

- **Como funciona:**  
  O LDR altera sua resistência conforme a luz.  
  - Ambiente claro → LED apagado  
  - Ambiente escuro → LED aceso

- **Conexões:**
  - LDR → GPIO34 (ADC)  
  - LED vermelho → GPIO2 (saída digital, com resistor em série)  
  - Divisor resistivo com LDR para leitura da luminosidade

- **Requisitos:** ESP32, MicroPython, LDR + resistor, LED + resistor, protoboard e jumpers

## Projeto 2 - Sensor Ultrassônico e LED de Intrusão

Este projeto detecta objetos próximos e aciona um **LED de alerta**.

- **Como funciona:**  
  O sensor ultrassônico mede a distância até objetos.  
  - Distância ≤ 10 cm → LED aceso + mensagem "INTRUSO DETECTADO!" no console  
  - Distância > 10 cm → LED apagado

- **Conexões:**
  - HC-SR04 TRIG → GPIO26  
  - HC-SR04 ECHO → GPIO25  
  - LED → GPIO27 (com resistor em série)  

- **Requisitos:** ESP32, MicroPython, HC-SR04, LED + resistor, protoboard e jumpers

---
## Projeto 3 - Sensor de Umidade do Solo e LED

Este projeto monitora a **umidade do solo** para plantas.

- **Como funciona:**  
  O sensor de umidade fornece um valor analógico.  
  - Solo úmido → LED apagado  
  - Solo seco → LED aceso

- **Conexões:**
  - Sensor de umidade → GPIO34 (ADC)  
  - LED → GPIO2 (saída digital, com resistor em série)  

- **Requisitos:** ESP32, MicroPython, LED + resistor, sensor de umidade, protoboard e jumpers

---

## Observações

- O **limiar de detecção** em cada sensor pode variar conforme o ambiente, sensor e solo. Ajuste os valores no código conforme necessário.
- Cada projeto possui vídeo de demonstração e fotos do circuito nas respectivas pastas.
- Todos os códigos foram desenvolvidos em **MicroPython**.

---

## Autores

- Ana Clara  
- Luiz dos Santos

---

Sinta-se à vontade para explorar cada projeto nas pastas correspondentes e adaptá-los para seus próprios experimentos com ESP32!
