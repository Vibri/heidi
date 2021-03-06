from rr_drone import *
import unittest

class RRDoneTest( unittest.TestCase ): 
  def testApprox4pts( self ):
    poly = [(983, 579), (261, 579), (262, 578), (266, 576), (314, 553), 
        (358, 534), (370, 529), (448, 498), (481, 488), (587, 460), (749, 460),
        (817, 485), (838, 494), (920, 536), (944, 552)]
    trapezoid = [(a[0][0], a[0][1]) for a in approx4pts( np.int0(poly) )]
    self.assertEqual( len(trapezoid), 4 )
    self.assertTrue( trapezoid, [(983, 579), (261,579), (587, 460), (749, 460)] )

  def testTrapezoid2line( self ):
    self.assertEqual( trapezoid2line( [(983, 579), (261,579), (587, 460), (749, 460)] ),
        [((983+261)/2,579), ((587+749)/2, 460)] )
    self.assertEqual( sorted(trapezoid2line( [(1246, 460), (1231, 570), (1152, 572), (1155, 460)] )),
        sorted([((1231+1152)/2,571), ((1246+1155)/2, 460)]) )

  def testProject2plane( self ):
    (x,y) = project2plane( imgCoord=(1280/2, 720/2), coord=(0.0, 0.0), height = 1.5,
        heading=math.radians(45), angleFB=math.radians(-30), angleLR=0 )
    self.assertAlmostEqual( x, y, 5 ) # because of 45 deg
    self.assertAlmostEqual( x, (1.5*math.sqrt(3))*(math.sqrt(2)/2.), 5 )
    self.assertEqual( project2plane( imgCoord=(1280/2, 720/2), coord=(0.0, 0.0), height = 1.5,
        heading=math.radians(45), angleFB=math.radians(0), angleLR=0 ), None )
    (x,y) = project2plane( imgCoord=(200, 720/2), coord=(0.0, 0.0), height = 1.5,
        heading=0, angleFB=0, angleLR=math.radians(-10) ) # angleLR is positive for turn right

  def testTrapezoid2lineBug( self ):
    "the line is oriented from drone to horizon"
    begin,end = trapezoid2line( [(739, 497), (690, 579), (316, 570), (631, 460)] )
    self.assertTrue( begin[1] > end[1] ) # in image coordinates

  def testRect2BLBRTRTL( self ):
    BL,BR,TR,TL = rect2BLBRTRTL( [(739, 497), (690, 579), (316, 570), (631, 460)] )
    self.assertEqual( BL, (316, 570) )
    sortedRect =  rect2BLBRTRTL( [(775, 565), (438, 577), (329, 466), (643, 460)] )

  def testRoadWidth( self ):
    self.assertEqual( roadWidth([(1.0, 0.0), (2.6, 0.5), (2.6, 5.0), (1.0, 6.0)]), 1.6 )
    self.assertAlmostEqual( roadWidth([(1.07, 3.69), (2.63, 2.57), (4.10, 5.08), (2.88, 6.02)]), 1.9, 1 )

if __name__ == "__main__":
  unittest.main() 

