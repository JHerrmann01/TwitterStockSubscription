import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;
public class App {
	private static int stockPrice;//gives the stock price
	public static String [] sources;// Gives x amount of Sources that we search and sends to user
	public static boolean rate; // Returns if stock is doing well for the day
	public static TwitterFactory a= new TwitterFactory();
	public static String nameStock;
	public static String nameSyb;
	public static boolean follow = true;
//Alan's twitter is @AlanYi6
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true)
		  .setOAuthConsumerKey("Aj53Yg5ijyCb0v6KxtunaIxV8")
		  .setOAuthConsumerSecret("VQb5UMxl2z3tryabee4s8fyh39VpzuY4yN9ThAGs3Uwd4voiha")
		  .setOAuthAccessToken("907456144297295872-wPrALDxqJiWjpe92JMUGlbft30kNqeH")
		  .setOAuthAccessTokenSecret("eHqZFhhM13ukT4ttJj7emBl6vE6wDCbZnIY6jRS5IdyCn");
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
	}
	
	public static String createTweet(Twitter twitter, String tweet) throws TwitterException {
		
	    Status status = twitter.updateStatus(tweet);
	    return status.getText();
	    
	}
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




//Follow back

	public static void followBack(boolean follow, String ID) throws TwitterException {
		Twitter twitter = a.getInstance();
		twitter.createFriendship(ID);
	}
}