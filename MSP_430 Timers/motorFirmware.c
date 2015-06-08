#include "msp430g2553.h"
#include "uartUtil.h"

#define CALDCO_UART  *(char *)0x10BE
#define CALBC1_UART  *(char *)0x10BF
 
int main(void) {
  WDTCTL = WDTPW | WDTHOLD; // Stop watchdog timer
  /* Use Factory stored presets to calibrate the internal oscillator */
  DCOCTL = 0;
  BCSCTL1 = CALBC1_1MHZ;
  DCOCTL = CALDCO_1MHZ;
   
  P1DIR |= BIT0 + BIT7;
  P2DIR |= BIT3 + BIT5; 
  P1OUT &= 0x00; 
  P2OUT &= 0x00; 
  P1SEL |= BIT1 | BIT2;
  P1SEL2 |= BIT1 | BIT2;
   
  /* Configure timer A as a clock divider to generate delay */
  TA0CCTL0 = CCIE;
  TA0CCTL1 = CCIE; // Enable counter interrupt on counter compare register 1
  TA0CCTL2 = CCIE;
  TA0CTL = TASSEL_2 + MC_1 + TAIE + ID_0; // Use the SMCLK to clock the counter, SMCLK/8, count up mode
  TA0CCR1 = 500;
  TA0CCR2 = 1000;
  TA0CCR0 = 20000;
  
  TA1CCTL0 = CCIE;
  TA1CCTL1 = CCIE; // Enable counter interrupt on counter compare register 1
  TA1CCTL2 = CCIE;
  TA1CTL = TASSEL_2 + MC_1 + TAIE + ID_0; // Use the SMCLK to clock the counter, SMCLK/8, count up mode
  TA1CCR1 = 1500;
  TA1CCR2 = 2000;
  TA1CCR0 = 20000;
   
  __enable_interrupt(); // Enable interrupts.
  //_BIS_SR(LPM0_bits + GIE); // Enter LPM0 with interrupts enabled
  
  Configure(104, 1, 0);
  
  while(1){
    unsigned char setChar = Read();
    switch(setChar){
      case 'a': TA1CCR1 = 100; 
                break;
      case 'b': TA1CCR1 = 400; 
                break;
      case 'c': TA1CCR1 = 800; 
                break;
      case 'd': TA1CCR1 = 1200; 
                break;
      case 'e': TA1CCR1 = 1600; 
                break;
      case 'f': TA1CCR1 = 2000; 
                break;
      default: TA1CCR1 = 1000;
    }
    Write(setChar);
  }
}
 
// TimerA interrupt service routine
#pragma vector = TIMER1_A0_VECTOR
__interrupt void CCR0_INT_1(void)
{
  P1OUT |= BIT0 + BIT7;
}

#pragma vector = TIMER1_A1_VECTOR
__interrupt void TAIV_INT_1(void)
{
  int switchInt = TA1IV;
  switch(switchInt) {
    case 2: P1OUT &= ~BIT0;
            break;
    case 4: P1OUT &= ~BIT7;
            break;        
    case 10: P1OUT |= BIT0 + BIT7;
            break;
  }
}

#pragma vector = TIMER0_A0_VECTOR
__interrupt void CCR0_INT_0(void)
{
  P2OUT |= BIT3 + BIT5;
}

#pragma vector = TIMER0_A1_VECTOR
__interrupt void TAIV_INT_0(void)
{
  int switchInt = TA0IV;
  switch(switchInt) {
    case 2: P2OUT &= ~BIT3;
            break;
    case 4: P2OUT &= ~BIT5;
            break;        
    case 10: P2OUT |= BIT3 + BIT5;
            break;
  }
}
