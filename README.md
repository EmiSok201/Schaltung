**

## Schaltung

**

**Beschreibung:**

Das Programm erstellt eine Elektrische Schaltung bestehen aus beliebig vielen Widerständen und einer Spannungsquelle. Des Weiteren werden die Spannungen und Ströme an den einzelnen Widerständen sowie der Gesamtwiderstand berechnet. Die Schaltung wird dabei in einem Plot Fenster visuell dargestellt. 

**Installation:**

**Verwendung:**

Zur Erstellung der Schaltung werden zu Beginn die Widerstände und die Spannungsquelle als Objekte erstellt. Hierfür dient die Klasse ***Resistor*** sowie ***VoltageSource***. 
Diese beiden Klassen erstellen ein Objekt eines Widerstandes bzw. einer Spannungsquelle mit dem gewünschten Ohm Wert bzw. Volt Wert. 

Anschließend wird  angeben wie die Widerstände in der Schaltung angeordnet sind. Dazu gibt man an welche Widerstände in Reihe oder parallel zueinander angeordnet sind.  Hierzu nutz man die Klasse ***Parallel*** und ***Series***. In diesen Klassen wird der Gesamtwiderstand berechnet je nachdem ob zwei Widerstände in Reihe oder Parallel zueinander geschaltet sind. Im Falle einer Reihenschaltung werden die Widerstandswerte addiert und im Falle einer Parallelschaltung werden die Kehrwerte der Widerstände addiert und davon nochmal der Kehrwert gebildet. 

Zur Berechnung der Spannungen und Ströme werden die zuvor erstellten Widerstände den jeweiligen Funktion übergeben. Im der Klasse ***ElectricalParameters*** befinden sich die Funktionen zur Berechnung der Spannungen und Ströme sowie die Berechnung des Widerstandes, sollte die Spannung und der Strom bereits bekannt sein. Zur Berechnung wird eine Objekt der Klasse ElectricalParameters*

**Beispiel:**

**Hinweise:**
