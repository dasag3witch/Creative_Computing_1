const int ledPins[] = {13, 12, 11};

String vocabulary[] = {"ready", "set", "go"};

int codes[][3] = {
    {0, 0, 1},  // ready
    {0, 1, 1},  // set
    {1, 1, 1}   // go
};

void setup() {
    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);
    pinMode(11, OUTPUT);
    
}

void loop() {

    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    delay(1000);
    
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    delay(1000);

    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    delay(1000);

    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    delay(1000);

    
}
