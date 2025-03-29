import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Container } from "@/components/Container";
import { Logo } from "@/components/Logo";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { ArrowLeft } from "lucide-react";

type Course = {
  courseCode: string;
  title: string;
  description: string;
  requirementsDescription: string;
};

type FormData = {
  subject: string;
  academic_level: string;
  term: string;
  past_courses: string;
};

const Recommendations = () => {
  const navigate = useNavigate();
  const [recommendations, setRecommendations] = useState<Course[]>([]);
  const [formData, setFormData] = useState<FormData | null>(null);

  useEffect(() => {
    // Retrieve recommendations from localStorage
    const storedRecommendations = localStorage.getItem("recommendations");
    const storedFormData = localStorage.getItem("formData");

    if (storedRecommendations) {
      setRecommendations(JSON.parse(storedRecommendations));
    } else {
      navigate("/form");
    }

    if (storedFormData) {
      setFormData(JSON.parse(storedFormData));
    }
  }, [navigate]);

  const formatAcademicLevel = (level: string) => {
    return level === "UG" ? "Undergraduate" : "Graduate";
  };

  return (
    <div className="min-h-screen bg-uw-white flex flex-col">
      <header className="bg-uw-black p-4">
        <div className="container mx-auto">
          <Logo />
        </div>
      </header>

      <Container className="flex-1">
        <div className="max-w-5xl mx-auto">
          <Button
            variant="outline"
            className="mb-6"
            onClick={() => navigate("/form")}
          >
            <ArrowLeft className="mr-2 h-4 w-4" /> Back to Form
          </Button>

          <h1 className="text-3xl font-bold mb-2">
            Your Course Recommendations
          </h1>

          {formData && (
            <div className="mb-8">
              <p className="text-muted-foreground mb-4">
                Based on your profile:{" "}
                <span className="font-medium">{formData.subject}</span> major,
                <span className="font-medium">
                  {" "}
                  {formatAcademicLevel(formData.academic_level)}
                </span>
                ,
              </p>
              <p className="text-sm text-muted-foreground">
                <span className="font-medium">Past courses:</span>{" "}
                {formData.past_courses}
              </p>
            </div>
          )}

          {recommendations.length === 0 ? (
            <div className="p-12 text-center bg-muted rounded-lg">
              <h3 className="text-xl font-medium">No recommendations found</h3>
              <p className="text-muted-foreground mt-2">
                Please try again with different criteria or check your past
                courses.
              </p>
              <Button
                onClick={() => navigate("/form")}
                className="mt-4 bg-uw-gold hover:bg-uw-gold/90 text-uw-black"
              >
                Try Again
              </Button>
            </div>
          ) : (
            <div className="grid md:grid-cols-3 gap-6">
              {recommendations.map((course) => (
                <Card key={course.courseCode} className="h-full flex flex-col">
                  <CardHeader className="pb-2">
                    <CardTitle className="flex flex-col">
                      <span className="text-uw-gold font-mono">
                        {course.courseCode}
                      </span>
                      <span className="text-xl mt-1">{course.title}</span>
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="flex-1">
                    <p className="text-gray-700 mb-4">{course.description}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          )}
        </div>
      </Container>

      <footer className="bg-uw-black text-uw-white p-4 text-center mt-auto">
        <p className="text-sm">
          © {new Date().getFullYear()} UW CourseMatch. All rights reserved.
        </p>
      </footer>
    </div>
  );
};

export default Recommendations;
