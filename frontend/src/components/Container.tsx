
import { cn } from "@/lib/utils";
import React from "react";

interface ContainerProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
}

export const Container: React.FC<ContainerProps> = ({ 
  children, 
  className,
  ...props
}) => {
  return (
    <div 
      className={cn("container mx-auto py-8", className)}
      {...props}
    >
      {children}
    </div>
  );
};
