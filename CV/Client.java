import java.io.*;
import java.net.*;
import edu.wpi.first.wpilibj.networktables.NetworkTable;

public class Client {
    public static void main(String[] args) {
        System.out.println("waiting");

        try{
            Socket soc=new Socket("localhost", 3341);
            BufferedReader inFromServer = new BufferedReader(new InputStreamReader (soc.getInputStream()));
            String fromServer;
            NetworkTable.setClientMode();
            NetworkTable.setIPAddress("roboRIO-3341-FRC.local");
            NetworkTable table = NetworkTable.getTable("cv");

            while(true){
                System.out.println("waiting");
                fromServer = inFromServer.readLine();

                if(fromServer != null){
                    System.out.println("RECEIVED: " + fromServer );

                    String[] parse = fromServer.split(":");

                    if(parse[0].equals("crossFound") || parse[0].equals("rectFound")){
                        table.putBoolean(parse[0], true);
                    }

                    if(parse[0].equals("crossAzi") || parse[0].equals("rectAzi")){
                        table.putNumber(parse[0], Double.parseDouble(parse[1]));
                    }
                }
            }
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
