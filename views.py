from django.shortcuts import render 
from django.shortcuts import HttpResponse

def mission_ccms(request):
    mission = """<i><strong>MISSION</strong></i> - The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in 
    the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national 
    development goals and standards of global excellence. """ 

    return HttpResponse(mission)

def vision_ccms(request):
    vision = """<i><strong>VISION</strong></i> - The College of Computing and Multimedia Studies
    shall be a center of excellence in delivering Computing and Multimedia education."""

    return HttpResponse(vision)

def objects_ccms(request):
    objects = """<i><strong>OBJECT</strong></i> - After graduation, alumni of MSEUF-CSS program shall:<br><br>
     
      1 . Be employed and demostrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions:<br>
       
      2. Emabark in lifelong learning or reseach to attune to the continuos innovation in the IT industry in order to adapt to 
      the changing demands of the global market: and<br>

      3. Exhibit leadership and teamwork, and commitment to thier respective local or global organizations.
         
            """
    
    return HttpResponse(objects)