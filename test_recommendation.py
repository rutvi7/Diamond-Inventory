import pytest
from unittest.mock import patch
from diamond_recommendation import DiamondRecommendationSystem

# Path to the diamonds dataset
DIAMONDS_CSV_PATH = 'diamonds.csv'

# Fixture to set up the recommendation system
@pytest.fixture
def recommendation_system():
    """Fixture to initialize the DiamondRecommendationSystem."""
    return DiamondRecommendationSystem(file_path=DIAMONDS_CSV_PATH)

# Test: Filter by cut
def test_filter_by_cut(recommendation_system):
    """Test filtering diamonds by cut."""
    filtered = recommendation_system.filter_diamonds(cut="Round")
    assert not filtered.empty, "Filtered results should not be empty."
    assert all(filtered['cut'].str.lower() == "round"), "All cuts should be 'Round'."

# Test: Filter by carat weight
def test_filter_by_carat_weight(recommendation_system):
    """Test filtering diamonds by carat weight."""
    filtered = recommendation_system.filter_diamonds(carat_weight=1.5)
    assert not filtered.empty, "Filtered results should not be empty."
    assert all(filtered['carat_weight'] == 1.5), "All carat weights should be 1.5."

# Test: Filter by multiple criteria
def test_filter_by_multiple_criteria(recommendation_system):
    """Test filtering diamonds by multiple criteria."""
    filtered = recommendation_system.filter_diamonds(cut="Oval", carat_weight=1.0, clarity="VS1")
    assert not filtered.empty, "Filtered results should not be empty."
    assert all(
        (filtered['cut'].str.lower() == "oval") &
        (filtered['carat_weight'] == 1.0) &
        (filtered['clarity'].str.lower() == "vs1")
    ), "Filtered results should match all given criteria."

# Test: No matches for invalid criteria
def test_no_matches(recommendation_system):
    """Test filtering with invalid criteria."""
    filtered = recommendation_system.filter_diamonds(cut="NonexistentCut")
    assert filtered.empty, "Filtered results should be empty for invalid criteria."

# Test: Validate cut input
def test_validate_cut(recommendation_system):
    """Test validation of diamond cut input."""
    assert recommendation_system.validate_cut("Round"), "Valid cut should pass validation."
    assert not recommendation_system.validate_cut("123!"), "Invalid cut should fail validation."

# Test: Validate carat input
def test_validate_carat(recommendation_system):
    """Test validation of carat weight input."""
    assert recommendation_system.validate_carat("1.5"), "Valid carat should pass validation."
    assert not recommendation_system.validate_carat("abc"), "Invalid carat should fail validation."

# Test: Validate clarity input
def test_validate_clarity(recommendation_system):
    """Test validation of diamond clarity input."""
    assert recommendation_system.validate_clarity("VS1"), "Valid clarity should pass validation."
    assert not recommendation_system.validate_clarity("!@#"), "Invalid clarity should fail validation."

# Test: Full workflow with mocked user input
def test_full_workflow_with_mocked_input():
    """Test the full recommendation workflow by mocking user input."""
    with patch("builtins.input", side_effect=["Round", "1.5", "VS1"]):
        recommendation_system = DiamondRecommendationSystem(DIAMONDS_CSV_PATH)
        filtered = recommendation_system.filter_diamonds(cut="Round", carat_weight=1.5, clarity="VS1")
        assert not filtered.empty, "Filtered results should not be empty."
