import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { toast } from "sonner";
import { Container } from "@/components/Container";
import { Logo } from "@/components/Logo";
import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { useRecommendations } from "@/hooks/useRecommendations";

const formSchema = z.object({
  subject: z.string().min(1, "Major is required"),
  academic_level: z.string().min(1, "Academic level is required"),
  past_courses: z.string().min(1, "Please enter at least one past course"),
});

type FormValues = z.infer<typeof formSchema>;

const RecommendationForm = () => {
  const navigate = useNavigate();
  const { getRecommendations, isLoading } = useRecommendations();
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const form = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      subject: "",
      academic_level: "",
      past_courses: "",
    },
  });

  const onSubmit = async (values: FormValues) => {
    setErrorMessage(null);
    const past_courses = values.past_courses
      .split(/[,\s]+/)
      .map((course) => course.trim())
      .filter((course) => course !== "");

    try {
      const data = await getRecommendations({
        subject: values.subject,
        academic_level: values.academic_level,
        past_courses: past_courses,
      });

      if (data && data.length > 0) {
        // Store recommendations in localStorage
        localStorage.setItem("recommendations", JSON.stringify(data));
        localStorage.setItem(
          "formData",
          JSON.stringify({
            ...values,
            past_courses: past_courses.join(", "),
          })
        );
        navigate("/recommendations");
      } else {
        setErrorMessage(
          "No recommendations found. Please try different criteria."
        );
        toast.error("No recommendations found", {
          description:
            "Please try different criteria or check your past courses.",
        });
      }
    } catch (error) {
      setErrorMessage(
        "An error occurred while fetching recommendations." + error
      );
      toast.error("Error", {
        description: "Failed to get recommendations. Please try again later.",
      });
    }
  };

  return (
    <div className="min-h-screen bg-uw-white flex flex-col">
      <header className="bg-uw-black p-4">
        <div className="container mx-auto">
          <Logo />
        </div>
      </header>

      <Container className="flex-1">
        <div className="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow-sm border border-uw-grey/30">
          <h1 className="text-3xl font-bold mb-6 text-center">
            Course Recommendation
          </h1>

          {errorMessage && (
            <div className="mb-6 p-4 bg-red-50 text-red-700 rounded-md">
              {errorMessage}
            </div>
          )}

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
              <FormField
                control={form.control}
                name="subject"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Major</FormLabel>
                    <Select
                      onValueChange={field.onChange}
                      defaultValue={field.value}
                    >
                      <FormControl>
                        <SelectTrigger>
                          <SelectValue placeholder="Select your major" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        <SelectItem value="CS">
                          Computer Science (CS)
                        </SelectItem>
                        <SelectItem value="MATH">Mathematics (MATH)</SelectItem>
                        <SelectItem value="STAT">Statistics (STAT)</SelectItem>
                        <SelectItem value="BUS">Business (BUS)</SelectItem>
                        <SelectItem value="ECON">Economics (ECON)</SelectItem>
                        <SelectItem value="ENG">Engineering (ENG)</SelectItem>
                        <SelectItem value="SCI">Science (SCI)</SelectItem>
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="academic_level"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Academic Level</FormLabel>
                    <Select
                      onValueChange={field.onChange}
                      defaultValue={field.value}
                    >
                      <FormControl>
                        <SelectTrigger>
                          <SelectValue placeholder="Select your academic level" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        <SelectItem value="UG">Undergraduate</SelectItem>
                        <SelectItem value="G">Graduate</SelectItem>
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                control={form.control}
                name="past_courses"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Past Courses</FormLabel>
                    <FormControl>
                      <Textarea
                        placeholder="Enter your past courses, separated by commas (e.g., CS135, MATH137, PHYS121)"
                        className="resize-none h-32"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <Button
                type="submit"
                className="w-full bg-uw-gold hover:bg-uw-gold/90 text-uw-black font-bold"
                disabled={isLoading}
              >
                {isLoading
                  ? "Getting Recommendations..."
                  : "Get Recommendations"}
              </Button>
            </form>
          </Form>
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

export default RecommendationForm;
