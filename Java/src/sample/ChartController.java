package sample;

import javafx.event.ActionEvent;
import javafx.fxml.*;
import javafx.scene.chart.AreaChart;
import javafx.scene.chart.XYChart;
import javafx.scene.control.*;

import java.net.URL;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;


public class ChartController implements Initializable {

    public static final String MENU_RESOURCE_LOCATION = "Menu.fxml";

    @FXML
    private AreaChart areaChart;


    public void initialize(URL url, ResourceBundle rb) {
        XYChart.Series series = new XYChart.Series<>();
        int i = 0;
        try {
            ResultSet resultSet = Database.getResultSet();
            series.setName("for next 7 days");
            while (resultSet.next()) {
                series.getData().add(new XYChart.Data("Day "+(i++),Double.parseDouble(resultSet.getString(1))));
            }
            areaChart.getData().clear();
            areaChart.getData().add(series);        } catch (SQLException e) {
            System.out.println("Aici am eroare!");
        }
    }

    @FXML
    public void goToPrediction() {
        GUI.getInstance().loadInterfaceFrom(MENU_RESOURCE_LOCATION);
    }

}