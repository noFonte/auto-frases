void setup() {
  Serial.begin(9600);  // Inicia a comunicação serial a 9600 baud
}

void loop() {
  int sensorValue = analogRead(A0);  // Lê o valor de um pino analógico
  Serial.println(sensorValue);       // Envia o valor pela porta serial
  delay(1000);                       // Aguarda 1 segundo
}