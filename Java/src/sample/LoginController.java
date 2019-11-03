package sample;
import javafx.event.ActionEvent;
import javafx.fxml.*;
import javafx.scene.control.*;
import java.net.URL;
import java.util.ResourceBundle;


public class LoginController implements Initializable{
	private static final String USERNAME = "admin";
	private static final String PASSWORD ="admin";
	private static final String ERROR_MESSAGE = "Incorrect username or password";
	private static final String VOID_MESSAGE = "";
	@FXML
	private TextField UserName;
	@FXML
	private PasswordField Password;
	@FXML
	private Button LoginButton;




	public void initialize(URL url, ResourceBundle rb){
		
	}

	@FXML
	public void login(ActionEvent actionEvent) {
		if(Password.getText().equals(PASSWORD)&&USERNAME.equals(UserName.getText()))
			GUI.getInstance().loadInterfaceFrom(MenuController.MENU_RESOURCE_LOCATION);
		else {
			UserName.setText(VOID_MESSAGE);
			Password.setText(VOID_MESSAGE);
			UserName.setPromptText(ERROR_MESSAGE);
			Password.setPromptText(ERROR_MESSAGE);
		}

	}
}