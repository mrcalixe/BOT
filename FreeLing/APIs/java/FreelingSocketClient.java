
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

/**
 * A simple client to communicate with Freeling "analyze --server"
 *
 */
public class FreelingSocketClient {
    private static final String SERVER_READY_MSG = "FL-SERVER-READY";
    private static final String RESET_STATS_MSG = "RESET_STATS";
    private static final String ENCODING = "UTF8";
    private static final String FLUSH_BUFFER_MSG = "FLUSH_BUFFER";
    private final static int BUF_SIZE = 2048;

    Socket socket;
    DataInputStream bufferEntrada;
    DataOutputStream bufferSalida;

    FreelingSocketClient(String host, int port) {
        try {            
            socket = new Socket (host, port); 
            socket.setSoLinger (true, 10);
            socket.setKeepAlive(true);
            socket.setSoTimeout(10000);  
            bufferEntrada = new DataInputStream (socket.getInputStream());
            bufferSalida = new DataOutputStream (socket.getOutputStream());
                        
            writeMessage(bufferSalida, RESET_STATS_MSG, ENCODING);
            
            StringBuffer sb=readMessage(bufferEntrada);
            if(sb.toString().replaceAll("\0", "").compareTo(SERVER_READY_MSG)!=0)
                System.err.println("SERVER NOT READY!");
            writeMessage(bufferSalida, FLUSH_BUFFER_MSG, ENCODING);
            readMessage(bufferEntrada);
            
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public String processSegment(String text) throws IOException {
        writeMessage(bufferSalida, text,ENCODING); 
        StringBuffer sb = readMessage(bufferEntrada);         
        writeMessage(bufferSalida, FLUSH_BUFFER_MSG, ENCODING);
        readMessage(bufferEntrada);
        return sb.toString();
    }

    public static void writeMessage(java.io.DataOutputStream out, String message, String encoding)
        throws IOException {
        out.write(message.getBytes(encoding));
        out.write(0);
        out.flush();
    }

    void close() throws IOException {
        socket.close();
    }

    private static synchronized StringBuffer readMessage(DataInputStream bufferEntrada)
        throws IOException {

        byte[] buffer = new byte[BUF_SIZE];     
        int bl =  0; 
        StringBuffer sb = new StringBuffer();

        //messages end with \0
        do { 
            bl =  bufferEntrada.read(buffer, 0, BUF_SIZE);
            if(bl>0) sb.append(new String (buffer,0,bl));
        } while (bl>0 && buffer[bl-1]!=0);

        return sb;
    }

    // replace this main with one that suits your needs.
    public static void main(String[]args) throws Exception {
        FreelingSocketClient server = new FreelingSocketClient("localhost", 50005);
        String s1 = server.processSegment("the cat eats fresh fish from the market.");
        System.out.println(s1);	   
        server.close();
    }
}
