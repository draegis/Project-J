import java.util.*; // Scanner , Locale
class Temperatures { 
public static void main (String[] args) 
	{
	System.out.println ("TEMPERATURES\n");
	// input tools 
	Scanner in = new Scanner (System.in); 
	in.useLocale (Locale.US);
	// enter the number of weeks and measurements 
	System.out.print ("number of weeks: "); 
	int nofWeeks = in.nextInt ();
	System.out.print ("number of measurements per week: "); 
	int nofMeasurementsPerWeek = in.nextInt ();
	// storage space for temperature data 
	double[][] t = new double[nofWeeks + 1][nofMeasurementsPerWeek + 1];
	// read the temperatures 
	for (int week = 1; week <= nofWeeks; week++) 
	{ 
		System.out.println ("temperatures - week " + week + ":");
		for (int reading = 1; reading <= nofMeasurementsPerWeek; reading++)
			t[week][reading] = in.nextDouble (); 
	} 
	System.out.println ();
	// show the temperatures 
	System.out.println ("the temperatures:"); 
	for (int week = 1; week <= nofWeeks; week++) 
	{ 
		for (int reading = 1; reading <= nofMeasurementsPerWeek; reading++) 
			System.out.print (t[week][reading] + " "); 
			System.out.println (); 
	} 
	System.out.println ();
	// the least , greatest and average temperature - weekly 
	double[] minT = new double[nofWeeks + 1]; 
	double[] maxT = new double[nofWeeks + 1]; 
	double[] sumT = new double[nofWeeks + 1]; 
	double[] avgT = new double[nofWeeks + 1];
	// compute and store the least , greatest and average // temperature for each week. // 
	for (int week = 1; week <= nofWeeks; week++)
	{
		double minTT = 300.0;
		double maxTT = -300.0;
		double sumTT = 0.0;
		int temp = 0;
		for (int reading = 1; reading <= nofMeasurementsPerWeek; reading++)
		{
			temp = reading + 1;
			if (t[week][reading] < minTT)
			{
				minTT = t[week][reading];
				if (t[week][temp] < t[week][reading])
					minTT = t[week][temp];
			}
			if (maxTT < t[week][reading]) {
				maxTT = t[week][reading];
				if (t[week][reading] < t[week][temp])
					maxTT = t[week][temp];
			}
			sumTT += t[week][reading];
		}
		minT[week] = minTT;
		maxT[week] = maxTT;
		sumT[week] = sumTT;
		avgT[week] = sumTT/nofMeasurementsPerWeek;
	}
	// show the least , greatest and average temperature for // each week // 
	for (int week = 1; week <= nofWeeks; week++)
	{
		System.out.println("Week " + week + " had a minimum temperatur of " + minT[week] );
		System.out.println("Week " + week + " had a maximum temperatur of " + maxT[week] );
		System.out.println("Week " + week + " had a sum temperatur of " + sumT[week] );
		System.out.println("Week " + week + " had a average temperatur of " + avgT[week] );
	}
	// the least , greatest and average temperature - whole period 
	double minTemp = minT[1];
	double maxTemp = maxT[1];
	double sumTemp = sumT[1]; 
	double avgTemp = 0;
	// compute and store the least , greatest and average // temperature for the whole period // 
	// show the least , greatest and average temperature for // the whole period // 
	
	}
}