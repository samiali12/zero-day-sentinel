from typing import Type
from pydantic import BaseModel, Field


class CVESearchToolInput(BaseModel):
    """Input for CVE Search Tool."""

    software_name: str = Field(
        ..., description="Name of te software to search for CVEs"
    )
    max_results: int = Field(5, description="Maximum number of CVE results to return")

class CVESearchTool(BaseModel):
    name: str = "CVE Search Tool"
    description: str = "Searches for recent Common Vulnerabilities and Exposures for specific software"
    args_schema: Type[BaseModel] = CVESearchToolInput

    def _run(self, software_name: str, max_results: int = 5) -> str:
        # Placeholder for actual CVE search logic
        # In a real implementation, this would query a CVE database or API
        dummy_cve_data = [
            {"id": "CVE-2023-0001", "description": f"Vulnerability in {software_name}"},
            {"id": "CVE-2023-0002", "description": f"Another vulnerability in {software_name}"},
            {"id": "CVE-2023-0003", "description": f"Yet another vulnerability in {software_name}"},
        ]
        results = dummy_cve_data[:max_results]
        return "\n".join([f"{cve['id']}: {cve['description']}" for cve in results])