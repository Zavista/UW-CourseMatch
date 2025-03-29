import { useState } from "react";

type Course = {
  courseCode: string;
  title: string;
  description: string;
  requirementsDescription: string;
};

type RecommendationRequest = {
  subject: string;
  academic_level: string;
  past_courses: string[];
};

export const useRecommendations = () => {
  const [isLoading, setIsLoading] = useState(false);

  const getRecommendations = async (
    request: RecommendationRequest
  ): Promise<Course[]> => {
    setIsLoading(true);

    const apiUrl = import.meta.env.VITE_API_URL || "http://localhost";
    const apiPort = import.meta.env.VITE_API_PORT || "8001";
    const endpoint = `${apiUrl}:${apiPort}/match`;

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch recommendations");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error fetching recommendations:", error);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  return {
    getRecommendations,
    isLoading,
  };
};
