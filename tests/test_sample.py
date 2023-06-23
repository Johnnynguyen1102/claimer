from claimer import paragraph
import pytest

@pytest.fixture
def example_data():
    return  {
            "id": "FK3",
            "text": "Face masks don’t work. Science in this area has evolved during the outbreak, the body of scientific evidence that has built up shows that the risk of transmission is made lower by wearing a face covering.  The more we learn about COVID-19 the clearer it is that face coverings are an absolute vital tool in our fight against the virus. They effectively capture droplets, which is the main way the virus travels from person to person. According to the British Medical Association, if you don't wear it and have COVID-19, the risk of spreading it to others can be as high as 70%. If you do wear it, the risk drops to 5%. Make sure you wear it in all public indoor spaces and whenever you can't keep a 2m distance from others. Use a face covering is simple and easy way we can all stop the spread of the virus.",
            "source": "www.rebeccaharris.org"
      }

def test_text1(example_data):    
    claims = paragraph.get_claims(example_data['text'])
    print("Sample:",example_data)
    for i,claim in enumerate(claims):
        print(f"{i}) {claim}")
    assert 8 == len(claims)