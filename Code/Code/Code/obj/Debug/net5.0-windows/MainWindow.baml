   M S B A M L   `   `   `  ����X  THelixToolkit.Wpf, Version=2.25.0.0, Culture=neutral, PublicKeyToken=52aa3500039caf0dM8clr-namespace:HelixToolkit.Wpf;assembly=HelixToolkit.WpfHelixToolkit.Wpf  5   	   ? ;Code, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullclr-namespace:CodeCode 5   	      Code.MainWindow   5   	   W SPresentationCore, Version=5.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=5.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=5.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5   	   R NSystem.Xaml, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   QHelixToolkit8clr-namespace:HelixToolkit.Wpf;assembly=HelixToolkit.Wpf     5   	   $localclr-namespace:Code     5   	   R NOxyPlot.Wpf, Version=2.1.2.0, Culture=neutral, PublicKeyToken=75e952ba404cdbb0Y UOxyPlot.Wpf.Shared, Version=2.1.2.0, Culture=neutral, PublicKeyToken=75e952ba404cdbb0"oxyhttp://oxyplot.org/wpf   5   	     � Title$  
MainWindow��5
   	   $	��450��6   $	��800��6)   .��5      �  � RowDefinitions 5   
   �� 5      $��* �6   �� 5      $��* �6    � ColumnDefinitions 5   
   �� 5      $��* �6   �� 5      $��* �6   .+�5   
   � $��0��6   $��0��6   
�������.+�5      �� $��State��6   $��Center=�6$   $��Center=�6A   5      � 5   
   $��0��6   $��1��6   
�������.+�5      �� .@�5      �� .��6   Info16%   �� 5      .��6   Info26%   5      5      � 5    
   $��1��6   $��0��6   
������.+�5!        OxyPlot.Wpf.PlotView  $��1��65     OxyPlot.Wpf.PlotViewBase   Model 6   �� *	MyModel+65   5"      � 5$   
   $��1��6   $��1��6   
�������.+�5%      &    HelixToolkit.Wpf.HelixViewport3D     ZoomExtentsWhenLoaded$
 True��6+      Children. 5&         HelixToolkit.Wpf.SunLight  g� 5'       g� Content 5(      � 5)       � Geometry 5*      k� 5+   "   -   5        meshMain�� k� 	Positions! �   	 k� TriangleIndices.	 �$        5.   #   
 � Material
 50      u� 51   "   -   5        matDiffuseMain�� u� Brush 52   &   �� 53   *    �� Color$
 Gray��6:   55   #   57      59      (   "HelixToolkit.Wpf.GridLinesVisual3D  5:         Width$ 8Q�61      Length$ 8Q�6;      MinorDistance$ 1Q�6F      MajorDistance$ 1Q�6X      	Thickness$
 0.01Q�6j   5;      5<      5=      5>      