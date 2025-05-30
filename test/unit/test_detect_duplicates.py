import pytest
from src.util import detector
# develop your test cases here



@pytest.mark.unit
@pytest.mark.parametrize('data, expected', [
  ([], ValueError), 
  (["frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"], [])
])
def test_detect_duplicates_invalid_input(data, expected):
  result = detector(data)
  assert result == expected

@pytest.mark.unit
@pytest.mark.parametrize('data, expected', [
  ([{"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer}"}, {"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer}"}], [{"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer}"}]), 
  ([{"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"}, {"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"}], [{"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"}]),
  ([{"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer}"}, {"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer}, doi={10.1007/s00766-023-00405-y}"}], [{"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"}]),
    ([{"frattini2002requirements,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"}, {"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"}], [{"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"}]), 
])
def test_detect_duplicates_duplicated_input(data, expected):
  result = detector(data)
  assert result == expected

@pytest.mark.unit
@pytest.mark.parametrize('data, expected', [
  ([{"frattini,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00405-y}"},{"frattini2002requirements,title={Requirements },author={Frattini},journal={Requirements Engineering},pages={1--14},year={2023},publisher={Springer},doi={10.1007/s00766-023-00401-y}"}], [])
])
def test_detect_duplicates_valid_input(data, expected):
  result = detector(data)
  assert result == expected