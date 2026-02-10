using System.ComponentModel.DataAnnotations;

namespace Assesment_6.Models
{
    public class Student
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Name is required")]
        public string Name { get; set; }

        [Required(ErrorMessage = "Email is required")]
        [EmailAddress(ErrorMessage = "Invalid email")]
        public string Email { get; set; }

        [Range(18, 30, ErrorMessage = "Age must be between 18 and 30")]
        public int Age { get; set; }
    }
}
