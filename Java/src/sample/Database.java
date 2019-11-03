package sample;

import java.sql.*;

public class Database {
    private static Database instance;
    private static final String DATABASE = "jdbc:sqlserver://localhost:1433;database=Statistica;integratedSecurity=true";
    private Connection connection;
    private static ResultSet resultSet = null;

    public static Database getInstance() {
        if (instance == null)
            instance = new Database();
        return instance;
    }

    private Database() {
        try {
            connection = DriverManager.getConnection(DATABASE);
        }
        // Handle any errors that may have occurred.
        catch (SQLException e) {
            System.out.println("Error at connecting to the database!");
            System.out.println(e.getMessage());
        }
    }

    public static void search(String companyName, String tableName) {
        try {
            Statement statement = instance.connection.createStatement();
            String selectSql = "SELECT Predictions.StockValue FROM [" + tableName + "] WHERE CompanyName = '" + companyName + "';";
            resultSet = statement.executeQuery(selectSql);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            System.out.println("Error at executing the search in the DATABASE!");
        }
    }

    public static ResultSet getResultSet() {
        return resultSet;
    }
}
