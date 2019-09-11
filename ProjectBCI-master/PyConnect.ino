char inputBuffer[10];
String inputString;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
  
  /*
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);*/
  Serial.write('1');
  
}

void loop() {
  
  while(!Serial.available()){}
  
  while(Serial.available()){

    if(Serial.available()>0){
      //digitalWrite(13,HIGH);
      char c = Serial.read();
      if(c != '\n')
      inputString += c;
    }
  }
  //Serial.print(inputString);
   //delay(2000);
   if(inputString.length() >0)
    {
      digitalWrite(13,LOW);
      Serial.print("Arduino received: ");  
      Serial.println(inputString); //see what was received

      Serial.print("String length: ");  
      Serial.println(inputString.length());
      /*if(inputString.equals("1")){             //One Blink
          Serial.println("One");
          digitalWrite(13,HIGH);
          digitalWrite(12,LOW);
          }
         else if(inputString.equals("2")){       //Two Blink
            Serial.println("Two");
            digitalWrite(13,LOW);
            digitalWrite(12,LOW);
          }*/
          
         if(inputString.equals("1")){     
            //Stop
            stopMotor();
          }
          else if(inputString.equals("2")){
            //Forward
            moveForward();
          }
          else if(inputString.equals("3")){
            //Turn Left and Move Forward
            turnLeft();
            //delay(500);
            //stopMotor();
            //moveForward();
          }
          else if(inputString.equals("4")){
            //Turn Right and Move Forward
            turnRight();
            //delay(500);
            //stopMotor();
            //moveForward();
          }
          
            inputString = "";
    }



/*

  // put your main code here, to run repeatedly:
  //while(true)
  {
    if(Serial.available() > 0){
      
        char c = Serial.read();
        
        if(c == '\n'){

            Serial.println("Input "+inputString);

            if(inputString.equals("ard")){            //Validate Arduino
            Serial.println("ard1");
            digitalWrite(13,HIGH);
            delay(2000);
            digitalWrite(13,LOW);
          }
        /*if(inputString.equals("1")){             //One Blink
          //Serial.println("One");
          digitalWrite(13,HIGH);
          digitalWrite(12,LOW);
          }
         else if(inputString.equals("2")){       //Two Blink
            //Serial.println("Two");
            digitalWrite(13,LOW);
            digitalWrite(12,LOW);
          }*/
/*         if(inputString.equals("1")){     
            //Stop
            stopMotor();
          }
          else if(inputString.equals("2")){
            //Forward
            moveForward();
          }
          else if(inputString.equals("3")){
            //Turn Left and Move Forward
            turnLeft();
            delay(500);
            moveForward();
          }
          else if(inputString.equals("4")){
            //Turn Right and Move Forward
            turnRight();
            delay(500);
            moveForward();
          }
          else{
            //Stop 
            stopMotor();
            }
            inputString = "";
          }
         else{
            inputString += c;
          }
    }
  }*/
}

void moveForward(){
    Serial.println("Forward");

    //Two wheels as forward
    /*digitalWrite(13,LOW);
    digitalWrite(12,HIGH);
    digitalWrite(11,HIGH);
    digitalWrite(10,LOW);*/
    
    //one small wheel as forward
    digitalWrite(13,HIGH);
    digitalWrite(12,LOW);
    digitalWrite(11,HIGH);
    digitalWrite(10,LOW);
    

    /*
    analogWrite(7, 153); // Run in half speed motor 1
    analogWrite(8, 255); // Run in full speed motor 2

    // change direction
 
    digitalWrite(7, LOW);
    digitalWrite(8, LOW);
    */
}

void turnLeft(){
  Serial.println("Left");
  //Two wheels as forward
  /*digitalWrite(13,HIGH);
  digitalWrite(12,LOW);
  digitalWrite(11,LOW);
  digitalWrite(10,LOW);*/

  //one small wheel as forward
  digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  digitalWrite(11,HIGH);
  digitalWrite(10,LOW);

}

void turnRight(){
  Serial.println("Right");
  //Two wheels as forward
  /*digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  digitalWrite(11,LOW);
  digitalWrite(10,HIGH);*/

  //one small wheel as forward
  digitalWrite(13,HIGH);
  digitalWrite(12,LOW);
  digitalWrite(11,LOW);
  digitalWrite(10,LOW);
  
}

void stopMotor(){
  Serial.println("Stop");
  
  digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  digitalWrite(11,LOW);
  digitalWrite(10,LOW);

}

