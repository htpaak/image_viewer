# 경로를 찾는 기능
# 프로그램 폴더와 사용자 데이터 폴더의 위치를 알려주는 함수들이 있어요.
import os  # 파일과 폴더를 다루는 도구
import sys  # 컴퓨터 시스템과 관련된 도구

def get_app_directory():
    """
    프로그램이 설치된 폴더를 찾아주는 함수예요.
    
    이 함수는 우리 프로그램이 어느 폴더에 있는지 알려줘요.
    프로그램이 설치 파일로 만들어졌을 때와 그냥 파이썬 코드로 
    실행할 때 다르게 동작해요.
    
    반환값:
        프로그램이 설치된 폴더의 경로
    """
    if getattr(sys, 'frozen', False):
        # 프로그램이 설치 파일로 만들어졌을 때
        return os.path.dirname(sys.executable)
    else:
        # 그냥 파이썬 코드로 실행할 때
        # core 폴더 안에 있으니까 바깥쪽 폴더를 찾아요
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_user_data_directory():
    """
    사용자의 정보를 저장할 폴더를 만들고 알려주는 함수예요.
    
    이 함수는 프로그램에서 사용자 정보(북마크, 설정 등)를 
    저장할 'UserData'라는 폴더를 찾아요. 
    만약 그 폴더가 없다면 새로 만들어줘요.
    
    반환값:
        사용자 데이터를 저장하는 폴더의 경로
    """
    app_dir = get_app_directory()  # 프로그램 폴더 찾기
    data_dir = os.path.join(app_dir, 'UserData')  # UserData 폴더 경로 만들기
    
    # 만약 그 폴더가 아직 없다면 새로 만들어요
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
        
    return data_dir  # 폴더 경로를 알려줌