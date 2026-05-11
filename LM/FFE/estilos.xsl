<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8" indent="yes" doctype-system="about:legacy-compat"/>

  <xsl:template match="/catalogo">
    <html lang="es">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title><xsl:value-of select="@tienda"/> - Catálogo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"/>
      </head>
      <body class="bg-light">
        
        <nav class="navbar navbar-dark bg-dark mb-4">
          <div class="container">
            <span class="navbar-brand mb-0 h1"><xsl:value-of select="@tienda"/></span>
            <span class="navbar-text text-white">
              Actualizado: <xsl:value-of select="@actualizado"/>
            </span>
          </div>
        </nav>

        <div class="container">
          <div class="row">
            
            <xsl:for-each select="juego">
              
              <xsl:sort select="nombre" order="ascending"/>
              
              <div class="col-12 col-md-6 col-lg-4 mb-4">
                
                <div class="card h-100 shadow-sm">
                  <div class="card-header bg-primary text-white">
                    <h5 class="card-title mb-0"><xsl:value-of select="nombre"/></h5>
                  </div>
                  
                  <div class="card-body">
                    <h6 class="card-subtitle mb-3 text-muted"><xsl:value-of select="editorial"/> - <xsl:value-of select="anio"/></h6>
                    <p class="card-text"><xsl:value-of select="descripcion"/></p>
                    
                    <ul class="list-group list-group-flush mb-3">
                      <li class="list-group-item px-0"><strong>Precio:</strong> <xsl:value-of select="precio"/> <xsl:value-of select="precio/@moneda"/></li>
                      <li class="list-group-item px-0"><strong>Jugadores:</strong> <xsl:value-of select="jugadores/@min"/>-<xsl:value-of select="jugadores/@max"/></li>
                      <li class="list-group-item px-0"><strong>Duración:</strong> <xsl:value-of select="duracion"/> <xsl:value-of select="duracion/@unidad"/></li>
                    </ul>

                    <xsl:choose>
                      <xsl:when test="stock &lt; 5">
                        <span class="badge bg-danger">Poco stock (<xsl:value-of select="stock"/>)</span>
                      </xsl:when>
                      <xsl:otherwise>
                        <span class="badge bg-success">En stock (<xsl:value-of select="stock"/>)</span>
                      </xsl:otherwise>
                    </xsl:choose>

                    <xsl:if test="estado = 'novedad'">
                      <span class="badge bg-warning text-dark ms-2">Novedad</span>
                    </xsl:if>
                    
                  </div>
                </div>
              </div>
              
            </xsl:for-each>
          </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>