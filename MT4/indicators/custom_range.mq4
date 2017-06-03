//+------------------------------------------------------------------+
//|                                                 custom_range.mq4 |
//|                                        inspired by Burton H. Pugh|
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "free"
#property link      "https://www.mql5.com"
#property version   "0.0.1"
#property strict
#property indicator_chart_window
#property indicator_buffers 5
//--- plot rangeTop
#property indicator_label1  "rangeTop"
#property indicator_type1   DRAW_HISTOGRAM
#property indicator_color1  clrNavajoWhite
#property indicator_width1  5
//--- plot rangeBottom
#property indicator_label2  "rangeBottom"
#property indicator_type2   DRAW_HISTOGRAM
//--- plot top
#property indicator_label3  "top"
#property indicator_type3   DRAW_LINE
#property indicator_style3  STYLE_SOLID
#property indicator_color3  clrRed
#property indicator_width3  2
//--- plot bottom
#property indicator_label4  "bottom"
#property indicator_type4   DRAW_LINE
#property indicator_style4  STYLE_SOLID
#property indicator_color4  clrLime
#property indicator_width4  2
//--- plot middle
#property indicator_label5  "middle"
#property indicator_type5   DRAW_LINE
#property indicator_style5  STYLE_SOLID
#property indicator_color5  clrDarkOrchid
#property indicator_width5  2
//--- input parameters
input double   fraction_numerator=1;
input double   fraction_denominator=3;
input int      period=26;
//--- indicator buffers
double         rangeTopBuffer[];
double         rangeBottomBuffer[];
double         topBuffer[];
double         bottomBuffer[];
double         middleBuffer[];
//--- global variables
double percentage;
//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
int OnInit()
  {
//--- indicator buffers mapping
   SetIndexBuffer(0,rangeTopBuffer);
   SetIndexBuffer(1,rangeBottomBuffer);
   SetIndexBuffer(2,topBuffer);
   SetIndexBuffer(3,bottomBuffer);
   SetIndexBuffer(4,middleBuffer);
//--- handle user input
   percentage = fraction_numerator / fraction_denominator;
   Print(percentage);
//---
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
  {
   int      i, ind;
   double half_amp;
//---
   // starting value is at least zero, so that the loop runs at least once (to handle the current bar)
   for(i = MathMax(rates_total - prev_calculated - 1, 0); i >= 0; i--)
   {
      // calculate top
      ind = iHighest(NULL,0,MODE_HIGH,period,i);
      if(ind != -1)
         topBuffer[i] = high[ind];
      else
         PrintFormat("Error in call iHighest. Error code=%d",GetLastError());

      // calculate bottom
      ind = iLowest(NULL,0,MODE_LOW,period,i);
      if(ind != -1)
         bottomBuffer[i] = low[ind];
      else
         PrintFormat("Error in call iLowest. Error code=%d",GetLastError());

      // calculate middle values
      half_amp = percentage * (topBuffer[i] - bottomBuffer[i]) / 2;
      middleBuffer[i] = (topBuffer[i] + bottomBuffer[i]) / 2;
      rangeTopBuffer[i] = middleBuffer[i] + half_amp;
      rangeBottomBuffer[i] = middleBuffer[i] - half_amp;
   }
//--- return value of prev_calculated for next call
   return(rates_total);
  }
//+------------------------------------------------------------------+
