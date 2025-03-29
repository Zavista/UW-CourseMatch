
import { Button } from "@/components/ui/button";
import { useNavigate } from "react-router-dom";
import { Container } from "@/components/Container";
import { Logo } from "@/components/Logo";
import { Separator } from "@/components/ui/separator";
import { Card, CardContent } from "@/components/ui/card";
import { ChevronRight, BookOpen, Lightbulb, Sparkles } from "lucide-react";

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-b from-uw-white to-gray-100 flex flex-col">
      <header className="bg-uw-black p-4 shadow-md">
        <div className="container mx-auto">
          <Logo />
        </div>
      </header>
      
      <Container className="flex-1 flex flex-col items-center justify-center text-center px-4 py-12 md:py-16">
        <div className="max-w-4xl w-full mx-auto">
          <div className="gold-gradient p-8 rounded-lg shadow-lg mb-10">
            <h1 className="text-4xl md:text-6xl font-bold mb-6 text-uw-black">
              UW <span className="text-uw-black">CourseMatch</span>
            </h1>
            <p className="text-lg md:text-xl mb-8 max-w-2xl mx-auto text-uw-black">
              Get personalized course recommendations based on your major and academic history. 
              Our AI-powered system helps you find the perfect courses for your next term.
            </p>
            <Button 
              onClick={() => navigate('/form')}
              className="bg-uw-black hover:bg-gray-800 text-uw-gold font-bold py-3 px-8 text-lg rounded-md transition-all duration-300 transform hover:scale-105"
            >
              Get Started <ChevronRight className="ml-2" />
            </Button>
          </div>

          <Separator className="my-8 bg-uw-gold h-0.5" />

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
            <Card className="bg-white shadow-md hover:shadow-lg transition-shadow duration-300">
              <CardContent className="p-6 flex flex-col items-center">
                <BookOpen className="h-12 w-12 text-uw-gold mb-4" />
                <h3 className="text-xl font-bold mb-2">Smart Recommendations</h3>
                <p className="text-gray-600">Courses tailored to your academic journey and interests</p>
              </CardContent>
            </Card>

            <Card className="bg-white shadow-md hover:shadow-lg transition-shadow duration-300">
              <CardContent className="p-6 flex flex-col items-center">
                <Lightbulb className="h-12 w-12 text-uw-gold mb-4" />
                <h3 className="text-xl font-bold mb-2">Discover New Paths</h3>
                <p className="text-gray-600">Explore courses you might not have considered before</p>
              </CardContent>
            </Card>

            <Card className="bg-white shadow-md hover:shadow-lg transition-shadow duration-300">
              <CardContent className="p-6 flex flex-col items-center">
                <Sparkles className="h-12 w-12 text-uw-gold mb-4" />
                <h3 className="text-xl font-bold mb-2">AI-Powered</h3>
                <p className="text-gray-600">Advanced algorithms to match your profile with the right courses</p>
              </CardContent>
            </Card>
          </div>
        </div>
      </Container>
      
      <footer className="bg-uw-black text-uw-white p-6 text-center">
        <div className="container mx-auto">
          <p className="text-sm mb-2">© {new Date().getFullYear()} UW CourseMatch. All rights reserved.</p>
          <p className="text-xs text-gray-400">Helping University of Waterloo students find their perfect academic path</p>
        </div>
      </footer>
    </div>
  );
};

export default Home;
