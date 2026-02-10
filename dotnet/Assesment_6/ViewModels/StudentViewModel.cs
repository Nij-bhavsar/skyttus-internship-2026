using System.ComponentModel.DataAnnotations;

namespace Assesment_6.ViewModels
{
    public class StudentViewModel
    {
        [Required]
        public string Name { get; set; }

        [Required]
        [EmailAddress]
        public string Email { get; set; }

        [Range(18, 30)]
        public int Age { get; set; }
    }
}
