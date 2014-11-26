import java.util.*; // Scanner , Locale

class Temperatures {
	public static void main(String[] args) {
		System.out.println("TEMPERATURES\n");
		// input tools
		Scanner in = new Scanner(System.in);
		in.useLocale(Locale.US);
		// enter the number of weeks and measurements
		System.out.print("number of weeks: ");
		int nofWeeks = in.nextInt();
		System.out.print("number of measurements per week: ");
		int nofMeasurementsPerWeek = in.nextInt();
		// storage space for temperature data
		double[][] t = new double[nofWeeks + 1][nofMeasurementsPerWeek + 1];
		// read the temperatures
		for (int week = 1; week <= nofWeeks; week++) {
			System.out.println("temperatures - week " + week + ":");
			for (int reading = 1; reading <= nofMeasurementsPerWeek; reading++)
				t[week][reading] = in.nextDouble();
		}
		System.out.println();
		in.close();
		// show the temperatures
		System.out.println("the temperatures:");
		for (int week = 1; week <= nofWeeks; week++) {
			for (int reading = 1; reading <= nofMeasurementsPerWeek; reading++)
				System.out.print(t[week][reading] + " ");
			System.out.println();
		}
		System.out.println();
		// the least , greatest and average temperature - weekly
		double[] minT = new double[nofWeeks + 1];
		double[] maxT = new double[nofWeeks + 1];
		double[] sumT = new double[nofWeeks + 1];
		double[] avgT = new double[nofWeeks + 1];
		// compute and store the least , greatest and average // temperature for
		// each week. //
		double minTT = 300.0; // Inital extreme values, this could be done by just assigning the first value instead.
		double maxTT = -300.0;
		for (int week = 1; week <= nofWeeks; week++) {
			double sumTT = 0.0;
			for (int reading = 1; reading <= nofMeasurementsPerWeek; reading++) {
				if (t[week][reading] < minTT) { // Will always be true for the first run, after that it's a normal comparison.
					minTT = t[week][reading];
				}
				if (t[week][reading] > maxTT) { // Same as above except reversed.
					maxTT = t[week][reading];
				}
				sumTT += t[week][reading]; // Simple addition for each week
			}
			minT[week] = minTT; // Each value is added for each week.
			maxT[week] = maxTT;
			sumT[week] = sumTT;
			avgT[week] = sumTT / nofMeasurementsPerWeek;
		}
		// show the least , greatest and average temperature for // each week //
		for (int week = 1; week <= nofWeeks; week++) {
			System.out.println("Week " + week + " had a minimum temperatur of "
					+ minT[week]);
			System.out.println("Week " + week + " had a maximum temperatur of "
					+ maxT[week]);
			System.out.println("Week " + week + " had a sum temperatur of "
					+ sumT[week]);
			System.out.println("Week " + week + " had a average temperatur of "
					+ avgT[week]);
		}
		// the least , greatest and average temperature - whole period
		double minTemp = 0;
		double maxTemp = 0;
		double sumTemp = 0;
		// compute and store the least , greatest and average // temperature for
		// the whole period //
		// show the least , greatest and average temperature for // the whole
		// period //
		// The for loop is not memory effective in any way shape or form. But it is easy to understand.
		double minTP = 300.0; // Initial extreme values
		double maxTP = -300.0;
		for (int week = 1; week <= nofWeeks; week++) {
			if (minT[week] < minTP) { // Will always be true the first run unless we are all dead
				minTP = minT[week]; // Simple process of just adding the lower value to a variable
			}
			if (maxT[week] > maxTP) { // Same as above except reversed
				maxTP = maxT[week];
			}
			sumTemp = sumTemp + sumT[week];
			minTemp = minTP; // A easy way to simplify the code, sure it's a horrible practice.
			maxTemp = maxTP; // But it gets the work done in a much simpler way.
		}
		System.out.println("The minimum temperature over the whole period was "
				+ minTemp);
		System.out.println("The maximum temperature over the whole period was "
				+ maxTemp);
		System.out
				.println("The sum of the temperature over the whole period was "
						+ sumTemp);
		System.out
				.println("The average of the temperature over the whole period was "
						+ sumTemp / (nofWeeks*nofMeasurementsPerWeek));
	}
}