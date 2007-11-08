import java.io.*;
import java.util.StringTokenizer;


// DWITE - October 2005 - Problem 4: Minesweeper
public class dwite200510p4 {
	
	public static void main(BufferedReader in, PrintWriter out) throws IOException {
		char[][] grid = readGridAndPad(in, 30, 16, ' ');
		calculateNeighbouringMines(grid);
		for (int i = 0; i < 5; i++)
			mainOnce(in, out, grid);
	}
	
	static void mainOnce(BufferedReader in, PrintWriter out, char[][] grid) throws IOException {
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		int y = Integer.parseInt(st.nextToken());
		int x = Integer.parseInt(st.nextToken());
		if (grid[y][x] == 'X')
			out.println("MINE - YOU LOSE");
		else if (grid[y][x] >= '1' && grid[y][x] <= '8')
			out.printf("NO MINE - %c SURROUNDING IT%n", grid[y][x]);
		else if (grid[y][x] == '0')
			out.printf("NO MINE - %d SQUARES REVEALED%n", reveal(grid, x, y, new boolean[grid.length][grid[0].length]));
		else
			throw new AssertionError();
	}
	
	
	static int reveal(char[][] grid, int x, int y, boolean[][] visited) {
		if (visited[y][x] || grid[y][x] == ' ')
			return 0;
		visited[y][x] = true;
		int result = 1;
		if (grid[y][x] == '0') {
			result += reveal(grid, x - 1, y - 1, visited);
			result += reveal(grid, x + 0, y - 1, visited);
			result += reveal(grid, x + 1, y - 1, visited);
			result += reveal(grid, x - 1, y + 0, visited);
			result += reveal(grid, x + 1, y + 0, visited);
			result += reveal(grid, x - 1, y + 1, visited);
			result += reveal(grid, x + 0, y + 1, visited);
			result += reveal(grid, x + 1, y + 1, visited);
		}
		return result;
	}
	
	static void calculateNeighbouringMines(char[][] grid) {
		for (int y = 1; y < grid.length - 1; y++) {
			for (int x = 1; x < grid[0].length - 1; x++) {
				if (grid[y][x] == '.')
					grid[y][x] = (char)(getMineNeighbourCount(grid, x, y) + '0');
			}
		}
	}
	
	static int getMineNeighbourCount(char[][] grid, int x, int y) {
		int count = 0;
		if (grid[y - 1][x - 1] == 'X') count++;
		if (grid[y - 1][x + 0] == 'X') count++;
		if (grid[y - 1][x + 1] == 'X') count++;
		if (grid[y + 0][x - 1] == 'X') count++;
		if (grid[y + 0][x + 1] == 'X') count++;
		if (grid[y + 1][x - 1] == 'X') count++;
		if (grid[y + 1][x + 0] == 'X') count++;
		if (grid[y + 1][x + 1] == 'X') count++;
		return count;
	}
	
	
	static char[][] readGridAndPad(BufferedReader in, int width, int height, char border) throws IOException {
		char[][] map = new char[height + 2][width + 2];
		for (int y = 1; y <= height; y++) {
			String line = in.readLine();
			for (int x = 1; x <= width; x++)
				map[y][x] = line.charAt(x - 1);
			map[y][0] = border;
			map[y][width + 1] = border;
		}
		for (int x = 0; x < width + 2; x++) {
			map[0][x] = border;
			map[height + 1][x] = border;
		}
		return map;
	}
	
	static String infile = "DATA41.txt";  // Specify null to use System.in
	static String outfile = "OUT41.txt";  // Specify null to use System.out
	
	public static void main(String[] args) throws IOException {
		InputStream in0;
		if (infile != null) in0 = new FileInputStream(infile);
		else in0 = System.in;
		Reader in1 = new InputStreamReader(in0, "US-ASCII");
		BufferedReader in = new BufferedReader(in1);
		
		OutputStream out0;
		if (outfile != null) out0 = new FileOutputStream(outfile);
		else out0 = System.out;
		Writer out1 = new OutputStreamWriter(out0, "US-ASCII");
		PrintWriter out = new PrintWriter(out1, true);
		
		main(in, out);
		
		in.close();
		in1.close();
		in0.close();
		out.close();
		out1.close();
		out0.close();
	}
}