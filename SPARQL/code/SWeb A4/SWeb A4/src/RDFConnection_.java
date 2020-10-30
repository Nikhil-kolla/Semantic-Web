import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.query.ResultSetFormatter;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdfconnection.RDFConnection;
import org.apache.jena.rdfconnection.RDFConnectionFactory;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import org.apache.jena.util.FileManager;

public class RDFConnection_ {

	public static void main(String[] args) throws IOException {
		
		//Reference for configuration file
		//https://medium.com/@sonaldwivedi/how-to-read-config-properties-file-in-java-6a501dc96b25
		Properties prop=new Properties();
		FileInputStream ip= new FileInputStream("C:\\Users\\hanum\\eclipse-workspace\\SWeb A4\\SWeb A4\\config.properties");
		prop.load(ip);
		//Reference for RDF Connection
		//https://github.com/apache/jena/blob/master/jena-rdfconnection/src/main/java/org/apache/jena/rdfconnection/examples/RDFConnectionExample6.java
		//RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create().destination("http://localhost:3030//Netflix.csv");
		RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create().destination(prop.getProperty("url"));
		
		Query query = QueryFactory.create("prefix Netflix: <http://netflix.org//Question//> "+
				                           " SELECT * "+
				                           "WHERE {"+  						  
				                           " ?s ?p ?o"+
				                           "}"
										 );
		try ( RDFConnectionFuseki conn = (RDFConnectionFuseki)builder.build() ) { 
		          conn.queryResultSet(query, ResultSetFormatter::out);
		}
		 
		
	    
	    String prefix_newmovies = "http://iiitd.ac.in/sweb/MT19123/newmoviesgraph";
	    Model model_newmovies = ModelFactory.createDefaultModel();
	    model_newmovies.setNsPrefix("NewMovies", prefix_newmovies);
	    
	    String prefix_oldmovies = "http://iiitd.ac.in/sweb/MT19123/oldmoviesgraph";
	    Model model_oldmovies = ModelFactory.createDefaultModel();
	    model_newmovies.setNsPrefix("NewMovies", prefix_oldmovies);
	    
	    String prefix_default = "http://netflix.org//Question//";
	    Model model = ModelFactory.createDefaultModel();
	    model.read(new FileInputStream(prop.getProperty("turtle_file")),null,"TTL");
	    
		
	}

}




// java -Xmx1200M -jar fuseki-server.jar --update -loc=Data /myDataset


