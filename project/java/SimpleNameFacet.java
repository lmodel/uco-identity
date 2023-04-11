package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  A simple name facet is a grouping of characteristics unique to the personal name (e.g., Dr. John Smith Jr.) held by an identity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SimpleNameFacet extends IdentityFacet {

  private List<String> familyName;
  private List<String> givenName;
  private List<String> honorificPrefix;
  private List<String> honorificSuffix;

}