package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  Birth information is a grouping of characteristics unique to information pertaining to the birth of an entity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BirthInformationFacet extends IdentityFacet {

  private String birthdate;

}