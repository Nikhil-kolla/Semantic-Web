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
import org.apache.jena.system.Txn;
import org.apache.jena.util.FileManager;

public class SWebA4Q1c
{
	public static void main(String[] args)throws FileNotFoundException,IOException
	{
		//Reference for configuration file
		//https://medium.com/@sonaldwivedi/how-to-read-config-properties-file-in-java-6a501dc96b25
		Properties prop=new Properties();
		FileInputStream ip= new FileInputStream("C:\\Users\\hanum\\eclipse-workspace\\SWeb A4\\SWeb A4\\config.properties");
		prop.load(ip);
		//Reference for RDF Connection
		//https://github.com/apache/jena/blob/master/jena-rdfconnection/src/main/java/org/apache/jena/rdfconnection/examples/RDFConnectionExample6.java
		try (RDFConnection connection = RDFConnectionFactory.connect(prop.getProperty("url"))){
			Txn.executeWrite(connection, ()->{
				//Creating Default graph making all the triples to this graph
				connection.update("PREFIX Netflix: <http://netflix.org//A4Q1//> "
						+"INSERT {?s ?p ?o } WHERE { SELECT * WHERE {?s ?p ?o}}");
				//Creating new named graph for new movies and inserting triples
				connection.update("PREFIX Netflix: <http://netflix.org//A4Q1//> "
						+"INSERT {GRAPH <http://iiitd.ac.in/sweb/MT19123/newmoviesgraph>{?s ?p ?o}}"
						+"WHERE {SELECT * WHERE { ?s Netflix:release_yearis ?y FILTER (?y>=\"2016\")"
						+"?s ?p ?o }}");
				//Creating new named graph for old movies and inserting triples
				connection.update("PREFIX Netflix: <http://netflix.org//A4Q1//> "
						+"INSERT {GRAPH <http://iiitd.ac.in/sweb/MT19123/oldmoviesgraph>{?s ?p ?o}}"
						+"WHERE {SELECT * WHERE { ?s Netflix:release_yearis ?y FILTER (?y<\"2016\")"
						+"?s ?p ?o }}");
				connection.load(prop.getProperty("triple_file"));
			
			});
			
		}
	}
}