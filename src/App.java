
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.*;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

import twitter4j.*;

	static String[] symbolArray = new String[] { 
			"MSFT", "AAPL", "GOOGL", "GOOG", "FB", "INTC", "CSCO", "ORCL", "SAP", "ADBE",
			"IBM", "CRM", "AVGO", "TXN", "NVDA", "VMW", "ADP", "QCOM", "INTU", "ITW", "BIDU", "MU",
			"INFY", "CTSH", "NOW", "WDAY", "AABA", "DELL", "AMAT", "HPQ", "NOK", "ADSK", "ETN", 
			"ATVI", "FISV", "EA", "RHT", "SQ", "XLNX", "LRCX", "NXPI", "WIT", "TEAM", "AMD", "TWTR",
			"MSI", "HPE", "MCHP", "AMZN" };
	
	static String[] stockNameArray = new String[] { 
			"Microsoft", "Apple", "Alphabet", "Alphabet", "Facebook", 
			"Intel", "Cisco Systems, Inc.", "Oracle", "SAP SE", "Adobe", "IBM", 
			"Salesforce", "Broadcom", "Texas Instruments Incorporated", "NVIDIA", 
			"Vmware", "ADP", "QUALCOMM", "Intuit", 
			"Illinois Tool Works Inc.", "Baidu", "Micron Technology", "Infosys Limited", 
			"Cognizant Technology Solutions Corporation", "ServiceNow", "Workday", "Altaba",
			"Dell", "Applied Materials", "HP", 
			"Nokia", "Autodesk", "Eaton", "Activision", 
			"Fiserv", "EA", "Red Hat", "Square", "Xilinx", 
			"Lam Research Corporation", "NXP Semiconductors N.V.", "Wipro Limited", "Atlassian Corporation Plc", 
			"Advanced Micro Devices, Inc.", "Twitter, Inc.", "Motorola Solutions", 
			"Hewlett Packard Enterprise Company", "Microchip Technology Incorporated", "Amazon" };
	
	static String NEWS_ARTICLE_API_KEY = "849198c20dc146dabe5508281d0912f7";
	
	
	//Sets API_KEY, SortBy Popular, and is only recent/top headlines as specified by the /top-headlines
	//To use this append the company name to this ENDPOINT
	static String NEWS_ARTICLE_ENDPOINT = "https://newsapi.org/v2/top-headlines" 
									+ "?apiKey=" + NEWS_ARTICLE_API_KEY
									+ "&sortBy=popularity"
									+ "&q=";
	
	static String GOOGLE_NATURAL_LANGUAGE = "https://language.googleapis.com/v1/documents:analyzeEntities";
	
	
=======
public class App {
	private static int stockPrice;//gives the stock price
	public static String [] sources;// Gives x amount of Sources that we search and sends to user
	public static boolean rate; // Returns if stock is doing well for the day
	public static TwitterFactory a= new TwitterFactory();
	public static String nameStock;
	public static String nameSyb;
	public static boolean follow = true;
//Alan's twitter is @AlanYi6
>>>>>>> 4d395c575add1b1ec847972e4375c8237349b3f2
	public static void main(String[] args) {
		
		/* Code for */
		
		
		
		
		
		// TODO Auto-generated method stub
<<<<<<< HEAD
		/*ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true)
		  .setOAuthConsumerKey("Aj53Yg5ijyCb0v6KxtunaIxV8")
		  .setOAuthConsumerSecret("VQb5UMxl2z3tryabee4s8fyh39VpzuY4yN9ThAGs3Uwd4voiha")
		  .setOAuthAccessToken("907456144297295872-wPrALDxqJiWjpe92JMUGlbft30kNqeH")
		  .setOAuthAccessTokenSecret("eHqZFhhM13ukT4ttJj7emBl6vE6wDCbZnIY6jRS5IdyCn");
=======
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true).setOAuthConsumerKey("Aj53Yg5ijyCb0v6KxtunaIxV8")
				.setOAuthConsumerSecret("VQb5UMxl2z3tryabee4s8fyh39VpzuY4yN9ThAGs3Uwd4voiha")
				.setOAuthAccessToken("907456144297295872-wPrALDxqJiWjpe92JMUGlbft30kNqeH")
				.setOAuthAccessTokenSecret("eHqZFhhM13ukT4ttJj7emBl6vE6wDCbZnIY6jRS5IdyCn");
>>>>>>> 4d395c575add1b1ec847972e4375c8237349b3f2
		TwitterFactory tf = new TwitterFactory(cb.build());
		Twitter twitter = tf.getInstance();

		try {
			String response = createTweet(twitter, tweetLayout());
			followBack(follow,"AlanYi6");
			//System.out.println(response);
			
			
		
			
		} catch (TwitterException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
<<<<<<< HEAD
		*/
		
		
		
		
		/*
		
		
		String response = "NOTHING!";
		try {
			response = getHTML();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println("Response: " + response);
		*/
		/*
		try {
			System.out.println("Response: " + getHTML(NEWS_ARTICLE_ENDPOINT + stockNameArray[0]));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		*/
		
		
		
		
		
=======

	}
	// If we make each person a separate class, put them into the parameter 
	public static String tweetLayout() {
		String layout= "";
		layout += nameStock + "\n";
		layout +=nameSyb + "\n";
		layout += stockPrice + "\n";
		/*for(int i =0; i<sources.length; i++) {
			layout += sources[i]+ "\n";
		}
		*/
		if(rate == true) {
			layout +="THIS STOCK IS LIT" + "\n";
		}
		else {
			layout +="Nawwww dawg don't buy this"+ "\n";
		}
		return layout;
>>>>>>> 4d395c575add1b1ec847972e4375c8237349b3f2
	}
	
	public static String createTweet(Twitter twitter, String tweet) throws TwitterException {
		
	    Status status = twitter.updateStatus(tweet);
	    return status.getText();
	    
	}
<<<<<<< HEAD
	
	
	
	public static String getHTML(String URI) throws Exception {
		StringBuilder result = new StringBuilder();
		  
		//Creating a URL
		URL url = new URL(URI);
		  
		//Establishing a connection to the given URL
		HttpURLConnection connection = (HttpURLConnection) url.openConnection();
		 
		//Distinguishing this connection as a GET request
		connection.setRequestMethod("GET");
		  
		//Building the response
		BufferedReader rd = new BufferedReader(new InputStreamReader(connection.getInputStream()));
		String line;
		while ((line = rd.readLine()) != null) {
		   result.append(line);
		}
		rd.close();
		return result.toString();
   }
	
	public static String (String URI, String Argument) throws Exception {
		
		String payload = "{\"document\":{\"type\":\"PLAIN_TEXT\", \"language\":\"EN\", \"content\":\"" + Argument + "\"}, \"encodingType\":\"UTF8\"}";
		CloseableHttpClient client = HttpClients.createDefault();
	    HttpPost httpPost = new HttpPost("http://www.example.com");
	 
	    String json = "{"id":1,"name":"John"}";
	    StringEntity entity = new StringEntity(json);
	    httpPost.setEntity(entity);
	    httpPost.setHeader("Accept", "application/json");
	    httpPost.setHeader("Content-type", "application/json");
	 
	    CloseableHttpResponse response = client.execute(httpPost);
	    assertThat(response.getStatusLine().getStatusCode(), equalTo(200));
	    client.close();
   }
	
=======
	//Creates the Structure of the DM
	
	public static String createDM() {
		String message= "";
		
		message += "The price of the stock is " + stockPrice + "\n" ;
		
	
	  	for(int i =0 ; i<sources.length; i++) {
	 
			message += sources[i];
		}
	
		if(rate == true) {
			message += "Good";
		}
		else {
			message +="bad";
		}
		
		return message;
		
	}
	
	//Sends the DM to the Person
	
	public static String sendDirectMessage(String recipientName, String msg) throws TwitterException {		
		
		Twitter twitter =a.getInstance();
		DirectMessage message = twitter.sendDirectMessage(recipientName, msg);
		return message.getText();
	}
>>>>>>> 4d395c575add1b1ec847972e4375c8237349b3f2




//Follow back

	public static void followBack(boolean follow, String ID) throws TwitterException {
		Twitter twitter = a.getInstance();
		twitter.createFriendship(ID);
	}
}
