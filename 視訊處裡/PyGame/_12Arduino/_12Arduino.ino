int switchPin1 = 4; 
int switchPin2 = 3;
void setup()
{
  // initialize serial comms
  pinMode(switchPin1, INPUT);
  pinMode(switchPin2, INPUT);
  Serial.begin(9600); 
}

void loop()
{
  // read A0
  int val1 = digitalRead(switchPin1);
  // read A1
  int val2 = digitalRead(switchPin2);
  // print to serial
  Serial.print(val1);
  Serial.print(" ");
  Serial.print(val2);
  Serial.print("\n");
  // wait 
  delay(50);
}
