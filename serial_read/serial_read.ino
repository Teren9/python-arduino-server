int incomingInt = 0;
int incomingByte = 0;
int incomingPortByte = 0;
String incomingString = "";
int ledState = LOW;
int sensor=0;

void setup() {
  Serial.begin(9600);
   
   for (int i=2; i<=13;i++){
      pinMode(i, OUTPUT); 

      digitalWrite(i, LOW);
    }
}

void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    delay(2);
    incomingPortByte = Serial.read();
    //incomingString  = Serial.readString();
    //incomingInt = Serial.parseInt();
    // say what you got:
    if (incomingByte == 'H'){
      digitalWrite(incomingPortByte, HIGH);
    }
    if (incomingByte == 'L'){
      digitalWrite(incomingPortByte, LOW);
      //digitalWrite(2, LOW);
    }
    if (incomingByte == 'R'){
      //delay(2);
      sensor = analogRead(incomingPortByte);
      Serial.println(sensor);
      //Serial.println("Hello world");
    }
  }

}
