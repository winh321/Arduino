
int pin=13;
char serialData;
void setup() {
  // put your setup code here, to run once:
pinMode(pin,OUTPUT);
Serial.begin(9600);
}

void loop() {
if(Serial.available()>0){
  serialData = Serial.read();
  Serial.print(serialData);
}

if(serialData == '1'){
digitalWrite(13,HIGH);
}

if(serialData == '0'){
  digitalWrite(13,LOW);
}

}
