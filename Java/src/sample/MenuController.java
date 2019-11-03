package sample;

import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.fxml.*;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ResourceBundle;


public class MenuController implements Initializable {

    public static final String MENU_RESOURCE_LOCATION = "Menu.fxml";
    private static final String LOGIN_RESOURCE_LOCATION = "Login.fxml";
    public static final String CHART_RESOURCE_LOCATION = "CompChart.fxml";
    public static final String TABLE_NAME = "Predictions";
    public static final String COCA_COLA_HBC = "Coca-Cola HBC";
    public static final String AVIVA = "Aviva";
    public static final String ROLLS_ROYCE = "Rolls-Royce";
    public static final String BARCLAYS = "Barclays";
    public static final String BRITISH_LAND_COMPANY = "British Land Company";
    public static final String COMPASS_GROUP = "Compass Group";
    public static final String HALMA = "Halma";
    public static final String UNILEVER = "Unilever";
    public static final String VODAFONE_GROUP = "Vodafone Group";
    public static final String NATIONAL_GRID = "National Grid";

    @FXML
    private Button LogOutBtn;


    public void initialize(URL url, ResourceBundle rb) {

    }

    @FXML
    public void gotoLogin(ActionEvent ev) {
        GUI.getInstance().loadInterfaceFrom(LOGIN_RESOURCE_LOCATION);
    }

    @FXML
    public void goToCocaColaHBCChart(Event actionEvent) {
        //TODO: Method to generate a resultSet
        Database.search(COCA_COLA_HBC, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void goToCompassGroupChart(ActionEvent actionEvent) {
        Database.search(COMPASS_GROUP, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void goToBarclaysChart(ActionEvent actionEvent) {
        Database.search(BARCLAYS, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void BritishLandCompany(ActionEvent actionEvent) {
        Database.search(BRITISH_LAND_COMPANY, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void goToAvivaChart(ActionEvent actionEvent) {
        Database.search(AVIVA, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void goToHalmaChart(ActionEvent actionEvent) {
        Database.search(HALMA, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void goToNationalGrillChart(ActionEvent actionEvent) {
        Database.search(NATIONAL_GRID, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void goToRollsRoyceChart(ActionEvent actionEvent) {
        Database.search(ROLLS_ROYCE, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void goToVodafoneGroupChart(ActionEvent actionEvent) {
        Database.search(VODAFONE_GROUP, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }

    public void goToUnileverChart(ActionEvent actionEvent) {
        Database.search(UNILEVER, TABLE_NAME);
        GUI.getInstance().loadInterfaceFrom(CHART_RESOURCE_LOCATION);
    }
}
