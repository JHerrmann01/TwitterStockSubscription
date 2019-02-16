import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Database {
	public static void main(String[] args) {
		// String jdbcDriver = "com.mysql.cj.jdbc.Driver";
		// String dbName = "TIGER";
		// try {
		// // public static void main(String[] args) throws Exception {
		// Class.forName(jdbcDriver);
		// Connection conn =
		// DriverManager.getConnection("jdbc:mysql://localhost/?user=root&password=");
		// Statement s = conn.createStatement();
		// int Result = s.executeUpdate("CREATE DATABASE " + dbName);
		// } catch (Exception e) {
		// e.printStackTrace();
		// }
		// // }
		// }
		try {
			String driver = "com.mysql.cj.jdbc.Driver";
			String url = "jdbc:mysql://localhost/";
			String username = "root";
			String password = "root";
			System.out.println("1");
			Class.forName(driver);
			System.out.println("2");
			Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/?user=root&password=");
			System.out.println("3");
			Statement st = conn.createStatement();
			String sql = "CREATE DATABASE STUDENTS";
			System.out.println("4");
			st.executeUpdate(sql);
			System.out.println("Created");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}