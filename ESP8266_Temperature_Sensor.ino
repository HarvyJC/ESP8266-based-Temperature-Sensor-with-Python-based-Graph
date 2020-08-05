const int sensor = A0; //Analog sensor (works both for ESP8266 and Arduino)
float temp, vout;

void setup() {
  Serial.begin(9600);

  start("HomeBro_ULTERA","mgajnh012418");

  pinMode(sensor, INPUT);
}

void loop() {
  vout = analogRead(sensor);
  temp = (vout*300)/1023; //Connect to 3V
  delay(1000);
}
