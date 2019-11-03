package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.*;
import javafx.stage.*;


public class GUI extends Application{
    private static GUI instance;
    private Stage guiStage;
    private Parent parent;
    public static final String DEFAULT_RESOURCE_LOCATION = "Login.fxml";

    public static GUI getInstance(){
        return instance;
    }

    public static void main(String[] args){
        launch(args);
    }

    public void start(Stage primaryStage){
        Thread connectToDB = new Thread() {
            @Override
            public void run() {
                Database.getInstance();
            }
        };
        connectToDB.start();
        instance = this;
        guiStage = primaryStage;
        loadInterfaceFrom(DEFAULT_RESOURCE_LOCATION);
    }

    public void loadInterfaceFrom(String pathToResource)
    {
        try {
            parent = FXMLLoader.load(getClass().getResource(pathToResource));
            Scene scene = new Scene(parent);
            guiStage.setScene(scene);
            guiStage.show();
        } catch (Exception e) {
            System.out.println(e.getStackTrace() );
            System.out.println("Eroare la incarcarea resursei spefificate");
        }
    }
}