/*
  ColorduinoPlasma - Plasma demo using Colorduino Library for Arduino
  Copyright (c) 2011 Sam C. Lin lincomatic@hotmail.com ALL RIGHTS RESERVED

  based on  Color cycling plasma
  Version 0.1 - 8 July 2009
  Copyright (c) 2009 Ben Combee.  All right reserved.
  Copyright (c) 2009 Ken Corey.  All right reserved.
  Copyright (c) 2008 Windell H. Oskay.  All right reserved.
  Copyright (c) 2011 Sam C. Lin All Rights Reserved

  This demo is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This demo is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/

#include "Colorduino.h"

enum Color { OFF, RED, BLUE, YELLOW };

unsigned char plasma[ColorduinoScreenWidth][ColorduinoScreenHeight];
long paletteShift;



float dist(float a, float b, float c, float d)  {
  return sqrt((c - a) * (c - a) + (d - b) * (d - b));
}



void plasma_morph() {
  unsigned char x, y;
  float value;
  ColorRGB colorRGB;
  ColorHSV colorHSV;

  for (y = 0; y < ColorduinoScreenHeight; y++)
    for (x = 0; x < ColorduinoScreenWidth; x++) {
      {
        value = sin(dist(x + paletteShift, y, 128.0, 128.0) / 8.0)
                + sin(dist(x, y, 64.0, 64.0) / 8.0)
                + sin(dist(x, y + paletteShift / 7, 192.0, 64) / 7.0)
                + sin(dist(x, y, 192.0, 100.0) / 8.0);
        colorHSV.h = (unsigned char)((value) * 128) & 0xff;
        colorHSV.s = 255;
        colorHSV.v = 255;
        Colorduino.HSVtoRGB(&colorRGB, &colorHSV);

        Colorduino.SetPixel(x, y, colorRGB.r, colorRGB.g, colorRGB.b);
      }
    }
  paletteShift++;

  Colorduino.FlipPage(); // swap screen buffers to show it
}



/********************************************************
  Name: ColorFill
  Function: Fill the frame with a color
  Parameter:R: the value of RED.   Range:RED 0~255
          G: the value of GREEN. Range:RED 0~255
          B: the value of BLUE.  Range:RED 0~255
********************************************************/
void ColorFill(unsigned char R, unsigned char G, unsigned char B) {
  ColorRGB *p = Colorduino.GetPixel(0, 0);
  for (unsigned char y = 0; y < ColorduinoScreenWidth; y++) {
    for (unsigned char x = 0; x < ColorduinoScreenHeight; x++) {
      p->r = R;
      p->g = G;
      p->b = B;
      p++;
    }
  }

  Colorduino.FlipPage();
}



void setup() {
  Colorduino.Init(); // initialize the board

  // compensate for relative intensity differences in R/G/B brightness
  // array of 6-bit base values for RGB (0~63)
  // whiteBalVal[0]=red
  // whiteBalVal[1]=green
  // whiteBalVal[2]=blue
  unsigned char whiteBalVal[3] = {63, 63, 63}; // for LEDSEE 6x6cm round matrix
  Colorduino.SetWhiteBal(whiteBalVal);

  /*
    // start with morphing plasma, but allow going to color cycling if desired.
    paletteShift=128000;
    unsigned char bcolor;

    //generate the plasma once
    for(unsigned char y = 0; y < ColorduinoScreenHeight; y++)
    for(unsigned char x = 0; x < ColorduinoScreenWidth; x++) {
      //the plasma buffer is a sum of sines
      bcolor = (unsigned char)
        (128.0 + (128.0 * sin(x*8.0 / 16.0)) +
         128.0 + (128.0 * sin(y*8.0 / 16.0))) / 2;
      plasma[x][y] = bcolor;
    }
  */
  // to adjust white balance you can uncomment this line
  // and comment out the plasma_morph() in loop()
  // and then experiment with whiteBalVal above
   ColorFill( 255, 255, 0 );
  //plasma_morph();

  // Do the serial comms
  Serial.begin( 9600 );
  
}


void loop() {
  //plasma_morph();
  
  
  if( Serial.available() > 0 ) {

    // A dummy counter to do somethig while the
    // loop waits for a good input
    int ctr = 0;
    while( Serial.parseInt() != -1 ) 
      ctr++;

    int changeTile[3] = {0};
    for( int i = 0; i < 3; i++ ) {
      changeTile[i] = Serial.parseInt();

      /*
      Serial.print( i, DEC );
      Serial.print( ": " );
      Serial.print( "I got a: " );
      Serial.println( changeTile[i], DEC ); */
     }
    ColorRGB outRGB = { 0, 0, 0 };
    switch( changeTile[2] ) {
      case RED:
        outRGB.r = 255;
        break;
      case BLUE:
        outRGB.b = 255;
        break;
      case YELLOW:
        outRGB.r = 255;
        outRGB.g = 255;
        break;
    }

    /*
    if( changeTile[0] >= 0 && changeTile[0] < ColorduinoScreenWidth 
     && changeTile[1] >= 0 && changeTile[1] < ColorduinoScreenHeight ) {
      
    }*/
    /*
    for( int i = 0; i < 3; i++ ) {
      Serial.print( changeTile[i] );
    }
    Serial.println( "" );
    Serial.println( outRGB.r );
    Serial.println( outRGB.g );
    Serial.println( outRGB.b );
    */
    Colorduino.SetPixel( changeTile[0], changeTile[1], outRGB.r, outRGB.g, outRGB.b );
    Colorduino.FlipPage();
    Colorduino.SetPixel( changeTile[0], changeTile[1], outRGB.r, outRGB.g, outRGB.b );
    Colorduino.FlipPage();
  }
  
  /*
    ColorFill( 0, 0, 32 );

    for( int x = 0; x < 4; x++ ) {
    for( int y = 0; y < 4; y++ ) {
      Colorduino.SetPixel( x, y, 0, 0, 0 );
    }
    }


    Colorduino.FlipPage();
    delay( 500 );
  */
}
