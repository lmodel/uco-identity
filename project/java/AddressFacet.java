package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  An Address Facet is a grouping of characteristics unique to an administrative identifier for a geolocation associated with a specific identity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AddressFacet extends IdentityFacet {

  private Location address;

}