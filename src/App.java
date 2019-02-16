import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;
public class App {

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
			String response = createTweet(twitter, "Testing out Twitter API :)");
			System.out.println(response);
		} catch (TwitterException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}
	
	public static String createTweet(Twitter twitter, String tweet) throws TwitterException {
	    Status status = twitter.updateStatus(tweet);
	    return status.getText();
	}

}
