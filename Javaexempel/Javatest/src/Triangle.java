import java.util.*; // Scanner , Locale

class Triangle {
	public static boolean e = true;
	public static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		int choice;
		do {
			System.out.println("1. Area Calculations\n2. Circumference Calculations\n3. Bisector Calculations\n4. Quit\n");
			System.out.println("Make a choice in the menu by entering a number: ");
			choice = in.nextInt();
			Triangle.Input(choice);
		} while (e);
	}

	public static double Area(double a, double b) {
		final double d = (a * b) / 2;
		return d;
	}

	public static double Circumference(double a, double b, double c) {
		double d = a + b + c;
		return d;
	}
	public static double Bisector(double b, double c, double alpha) 
	{ 
		double p = 2 * b * c * Math.cos (alpha / 2); 
		double bis = p / (b + c);
		return bis;
	}
	public static void Turnoff() {
		Triangle.e = false;
	}

	public static void Input(int choice) 
	{
		switch (choice) 
		{
		case 1:
			System.out.println("Enter the base and height of your triangle: ");
			double[] area = new double[2];
			for (int i = 0; i < area.length; i++) 
			{
				area[i] = Triangle.in.nextDouble();
			}
			double aread = Triangle.Area(area[0], area[1]);
			System.out.println("Your triangles area is: " + aread + "\n");
			break;
		case 2:
			System.out.println("Enter all of your triangles sides: ");
			double[] circ = new double[3];
			for (int i = 0; i < circ.length; i++) 
			{
				circ[i] = Triangle.in.nextDouble();
			}
			double circu = Triangle.Circumference(circ[0], circ[1], circ[2]);
			System.out.println("Your triangles circumference is: " + circu + "\n");
			break;
		case 3:
			System.out.println("Enter the two sides: ");
			double[] bis = new double [2];
			for (int i = 0; i < bis.length; i++)
			{
				bis[i] = Triangle.in.nextDouble();
			}
			System.out.println("Enter the angle between the sides: ");
			double angle = Triangle.in.nextDouble();
			double bisu = Triangle.Bisector(bis[0], bis[1], angle);
			System.out.println("Your bisectors length is: " + bisu + "\n");
			break;
		case 4:
			in.close();
			Triangle.Turnoff();
		}
	}
}