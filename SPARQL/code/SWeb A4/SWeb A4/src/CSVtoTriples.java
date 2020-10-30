import java.io.FileOutputStream;
import java.io.FileReader;
import java.util.Arrays;

import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.ResourceFactory;
import org.apache.jena.tdb.base.objectfile.StringFile;
import org.apache.jena.vocabulary.RDF;
import org.apache.jena.vocabulary.RDFS;

import com.fasterxml.jackson.annotation.JsonTypeInfo.Id;
//import com.fasterxml.jackson.databind.ser.std.StdKeySerializers.EnumKeySerializer;

import org.apache.jena.datatypes.xsd.XSDDatatype;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.RDFNode;
import org.apache.jena.rdf.model.ResourceFactory;

import au.com.bytecode.opencsv.CSVReader;

public class CSVtoTriples {

	public static void main(String[] args) throws Exception {
		
		//Reference :- https://www.javatpoint.com/java-filereader-class
		FileReader fr = new FileReader("C:\\Users\\hanum\\Desktop\\NetflixList.csv");
		//Reference :- javatpoint.com/how-to-read-csv-file-in-java
		CSVReader reader =new CSVReader(fr);
		
		//String[] titles;
		String[] entries = reader.readNext();
		int i=0;
		while(i<entries.length)
		{
			entries[i]=entries[i]+"is";
			i++;
		}		
		String prefix = "http://netflix.org//A4Q1//";
		Model model = ModelFactory.createOntologyModel();
		model.setNsPrefix("Netflix", prefix);
		
		Resource typeClass = ResourceFactory.createResource("http//www.netflix.org/entertainmentMedium");
		Resource movie = ResourceFactory.createResource("http//www.netflix.org/movie");
		Resource tvshow = ResourceFactory.createResource("http//www.netflix.org/tvshow");
		
		
		String getRow[];
		String finaltitle;
	
		while( (getRow = reader.readNext()) != null )
		{
			
			finaltitle = getRow[2].replace(' ','_');
			Resource typeDivision = model.createResource(prefix + finaltitle);
			for(int j=0;j< getRow.length;j++)
			{
				Property prop_is = model.createProperty(prefix + entries[j]);
				if(j == 2)
				{
					continue;
				}
				if(j == 0)
				{	
					typeDivision.addProperty( prop_is , model.createLiteral(getRow[0]));
				}else if(j == 1)
				{
					if( getRow[j].equals("Movie"))
					{
						model.add(prop_is,RDF.type,"Movie");
						typeDivision.addProperty(prop_is, model.createLiteral("Movie"));
					}
					else
					{
						model.add(prop_is,RDF.type,"TV Show");
						typeDivision.addProperty(prop_is, model.createLiteral("TV Show"));
					}
				}
				else
				{
					
					String[] each = getRow[j].split(",");
					for(int k = 0; k<each.length;k++)
					{
						typeDivision.addProperty(prop_is, model.createLiteral(each[k]));
					}	
				}	
			}
		}
		model.write(System.out,"TURTLE");		
		model.write(new FileOutputStream("C:\\Users\\hanum\\Desktop\\NetflixTriples.ttl"), "TURTLE");
	}
}





